from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import base64
import json
import binascii

class Encryption:
    @property
    def encrypt_method(self):
        return "AES-256-CBC"

    @property
    def encrypt_method_length(self):
        return int(self.encrypt_method.split('-')[1])

    @property
    def encrypt_key_size(self):
        return self.encrypt_method_length // 8

    def decrypt(self, encrypted_data, password):
        try:
            # Base64 decode the input data
            encrypted_data = base64.b64decode(encrypted_data)
            # Convert back to string
            json_data = json.loads(encrypted_data.decode('utf-8'))
            
            # Extract salt, iv, and ciphertext from the JSON
            salt = binascii.unhexlify(json_data['salt'])
            iv = binascii.unhexlify(json_data['iv'])
            ciphertext = base64.b64decode(json_data['ciphertext'])
            iterations = int(json_data['iterations'])
            if iterations <= 0:
                iterations = 999

            # Debugging: print the key parameters
            print(f"Salt (hex): {binascii.hexlify(salt).decode()}")
            print(f"IV (hex): {binascii.hexlify(iv).decode()}")
            print(f"Ciphertext (base64): {json_data['ciphertext']}")
            print(f"Iterations: {iterations}")
            
            # Derive the key using PBKDF2
            key = PBKDF2(password, salt, dkLen=self.encrypt_key_size, count=iterations)

            # Debugging: print the derived key
            print(f"Derived Key (hex): {binascii.hexlify(key).decode()}")

            # Create the AES cipher
            cipher = AES.new(key, AES.MODE_CBC, iv)

            # Decrypt the ciphertext
            decrypted = cipher.decrypt(ciphertext)
            
            # Debugging: print the decrypted bytes before unpadding
            print("Decrypted data before unpadding:", decrypted)

            # Return decrypted data without unpadding
            return decrypted
        except (ValueError, KeyError, binascii.Error) as e:
            print("Error during decryption:", str(e))
            return None


# Example usage
encryption = Encryption()
nonce_value = 'mI4DwthFYmcefl7V'
readable_string = "eyJjaXBoZXJ0ZXh0IjoiUzlXbjNNKzRcL3VvTGtDZkNvVEd3cmYxNmxhVXgzdkJVa1RNaG5TWmNDYkk9IiwiaXYiOiI0MjIyZTI0NjEyNzg5Mjg2M2NmMTIyNjE4MDQ3NGUyNiIsInNhbHQiOiIzZjIxYTRiMmRjZTE2YzVkYmZjYzZkZjUzZmEwYzFkNWUyNDIyODk4YjZmYTk5YzE2ZGE3NjU2MGE3YjUwZTU2ZjNiN2MzOTM2NjYyNDExYTRiNjRlZjM3ZDljYjI0NWY4ZjJkYzE4Y2ZmNmIwNjY2MDA1Yzk1YTVhNjE3NDE1MWI4ZTAwMDIyNzQ4MTI4MWFmYjQyMGUyZGJkNmE4ZjlhNDgwYTg0ZGY0NTgzZDA5MWU5MDNiZTYxNTc4YzFlYjZjNWNjZWZhNmRmODc1Mjk3Y2M4NDExOThkZDUzMjAzMzkyN2RlYTMzZDJiZTU1NTkwZGY4Mzg5Mzk5MDM0NmRmMjNmNDcyZTY3NGJiNGU2NzYzNmIzOGY3M2NkZDA3Yzc3YWY2OWRlOTY1ZTNmZmNkMmJjYzYxZjE4MWFjN2U0ODU2MjQ0YjQ3NGM1NWZkNGNjNjdhNjg4ZDM3Yzg1Y2IyZmE0ODg5ZGFmZGNlNGYzYjEzMmUzYTE1Zjk2ODRiYWZhNDI0YzIzZWQ1ZGRhMGI1NzdlMjE3YjY0NWIzNzM3MmQ0ZDFkYTMzMzRmYzg5OTcyODU3MjlkY2NlMmI4MjczNjczM2RhY2Y0NTQ3MTZjZjQ4YmMxZmM2OGI1MjJjZDFhYzhhYTEwMzFjMWZlYzgzMzQwMmViNGFkZGY2YzlhZiIsIml0ZXJhdGlvbnMiOjk5OX0="
decrypted = encryption.decrypt(readable_string, nonce_value)
print("Decrypted result:", decrypted)
