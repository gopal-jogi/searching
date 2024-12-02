from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad, pad
import base64
import json
import binascii
import os

class Encryption:
    def encrypt_method_length(self):
        return 256  # AES-256 uses 256-bit keys

    def encrypt_key_size(self):
        return int(self.encrypt_method_length() / 8)

    def encrypt_method(self):
        return "AES-256-CBC"

    def decrypt(self, encrypted_data, password):
        try:
            # Decode the base64-encoded input string
            encrypted_data = base64.b64decode(encrypted_data)
            json_data = json.loads(encrypted_data.decode('utf-8'))

            # Extract salt, iv, and ciphertext
            salt = binascii.unhexlify(json_data['salt'])
            iv = binascii.unhexlify(json_data['iv'])
            ciphertext = base64.b64decode(json_data['ciphertext'])
            iterations = int(json_data['iterations'])
            if iterations <= 0:
                iterations = 999

            # Derive the key using PBKDF2
            key_size = self.encrypt_key_size()
            key = PBKDF2(password, salt, dkLen=key_size, count=iterations)

            # Decrypt using AES
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = cipher.decrypt(ciphertext)

            # Debugging: print decrypted raw bytes before unpadding
            print("Decrypted raw data (before unpadding):", decrypted_data)

            # Try to unpad the data
            try:
                return unpad(decrypted_data, AES.block_size).decode('utf-8')
            except ValueError as ve:
                # Padding issue, return decrypted data as raw bytes
                print(f"Padding error: {ve}")
                return decrypted_data.decode('utf-8', errors='replace')

        except Exception as e:
            print(f"Error during decryption: {e}")
            return None

    def encrypt(self, plaintext, password):
        # Generate random salt and IV
        salt = os.urandom(32)
        iv = os.urandom(16)

        # Derive the key
        key_size = self.encrypt_key_size()
        key = PBKDF2(password, salt, dkLen=key_size, count=999)

        # Encrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

        # Create the result structure
        encrypted_data = {
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
            'iv': binascii.hexlify(iv).decode('utf-8'),
            'salt': binascii.hexlify(salt).decode('utf-8'),
            'iterations': 999
        }

        # Convert to JSON and Base64-encode the result
        return base64.b64encode(json.dumps(encrypted_data).encode('utf-8')).decode('utf-8')

# Example usage
encryption = Encryption()
nonce_value = 'mI4DwthFYmcefl7V'
readable_string = "eyJjaXBoZXJ0ZXh0IjoiU0p5aTRlOFpIUlNoR0tHSW1YWUhiQT09IiwiaXYiOiI4MzQ4NGM3NmJlZDNlN2M0NGVkYTRhZTgzOGQ3YWE3MiIsInNhbHQiOiJhM2JlOGE2N2Q2YTZiOTNhMDVlYTM0MDY1NDJiODZkOWE1Mjc0ZGZiYjNlMzAzNTU4OTlmNzE1MThjMTFlYjljNDAwMDc0ZGI3YTc1MDc0M2YwZDhmZDFkYTA5ZGRjNWM2NTY1ZjIwNjRjMjBiYmE2Yzc5ZjQ0NTUxMjFmOTk4ODI3YzliOWVhOTg1ODc5NDVmOGI4ZTdlZjJmNDFmNTVhYjgyZDZiYjg5YWRhMWQzMTk1Y2E3NDMxYzNlYWE1MGE5ODE5NzJhZjVlMjdiMzg0MTE2Y2U1ZTkyNzcyNWY2YWFiMWFhYmIzOGZiOGNjMTdkOWQxZjc4MzA0ZjAzYjE0MTg0NThjNzhiZWJiNDk1NTZmZjk0ZmM1MWQwOGY0ZDQwOWRmNDhiNmZlNGUyNTc5NGVkZmUzOTE2MjRiZjcxNjA1YjhjOGU4NDI0NDVjYmY4OGRhODcxMmQ4ZDExNGQwYzdiY2RkNjZlOWQyY2JjY2I2ZjM1YTVmZDcyOTQ0NDg1MzIzZDc5YzY0NGJlNzA2NjM0ZTBmNDI2ODU3Zjg0ZTU4MzljMmJmMGI5MDYxY2Q2ZjdhNzlhOWVlMzZlOThmMzk1MTBlNDEwYzVkNWZmYTVhOTJiMTMyZDkzOWZjNDIwNTU2ZTIwZWFlODA1YThkMjFjMTliYzIwMDJjZWMzMSIsIml0ZXJhdGlvbnMiOjk5OX0="
decrypted = encryption.decrypt(readable_string, nonce_value)
print("Decrypted data:", decrypted)
