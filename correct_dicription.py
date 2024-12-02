import base64
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512

class Encryption:
    def __init__(self):
        self.encrypt_method = "AES-256-CBC"
    
    @property
    def encrypt_method_length(self):
        return int(self.encrypt_method.split('-')[1])

    @property
    def encrypt_key_size(self):
        return self.encrypt_method_length // 8

    def decrypt(self, enc_data, password):
        # Base64 decode the input data
        enc_data = base64.b64decode(enc_data)
        enc_data = json.loads(enc_data.decode('utf-8'))

        # Extract the salt, IV, and ciphertext
        salt = bytes.fromhex(enc_data['salt'])
        iv = bytes.fromhex(enc_data['iv'])
        ciphertext = base64.b64decode(enc_data['ciphertext'])
        iterations = int(enc_data['iterations'])

        # Derive key from password
        key = PBKDF2(password, salt, dkLen=self.encrypt_key_size, count=iterations, hmac_hash_module=SHA512)

        # Decrypt the ciphertext
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted = cipher.decrypt(ciphertext)

        # Remove padding (PKCS7)
        padding_len = decrypted[-1]
        decrypted = decrypted[:-padding_len]

        return decrypted.decode('utf-8')

    def encrypt(self, plaintext, password):
        # Generate random salt and IV
        salt = get_random_bytes(32)  # 256 bits
        iv = get_random_bytes(16)  # 128 bits

        # Derive key from password
        key = PBKDF2(password, salt, dkLen=self.encrypt_key_size, count=999, hmac_hash_module=SHA512)

        # Encrypt the plaintext
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_plaintext = self._pad(plaintext.encode('utf-8'))
        ciphertext = cipher.encrypt(padded_plaintext)

        # Encode the output as Base64 and return
        enc_data = {
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
            'iv': iv.hex(),
            'salt': salt.hex(),
            'iterations': 999
        }

        enc_json = json.dumps(enc_data)
        return base64.b64encode(enc_json.encode('utf-8')).decode('utf-8')

    def _pad(self, s):
        padding_len = AES.block_size - len(s) % AES.block_size
        return s + bytes([padding_len]) * padding_len

# Usage
encryption = Encryption()

# Decryption example
nonce_value = 'mI4DwthFYmcefl7V'
readable_string = "eyJjaXBoZXJ0ZXh0IjoiUUVSNk1UNGVIMnNXOEVPU1NXMFhoUT09IiwiaXYiOiJlZjkwNzQ0NWEyYWNiNzIxYWQzZjAwNjFhYjJiYjBhNCIsInNhbHQiOiI1NWRkMjk2MmI2YWIwZWZmNDZhYWMxNWE1YzE3MGY4ZDEyNjM3YzkxZjZhZmY4MDg4MDc2M2ZhNGRiZTI3ZmUxNGMxNDg4OWQ0ZTZlNjBhNmQxZmYxMjE1ZDJjNzBiYWMwYTg5NDc2M2QzMTg5M2MwOGY0NjhkNGIxODk2M2RjM2U2M2JhNjk0ODJhYjE2NmI2NjBiZTRmMTU1ZmQ4OTM3ZWE5OTQzOTMzNmVmMmZiZTNiZjFlOGRhYWY5NTUzNWQ3NTQ2YzdjODllMmU5NTdlYjRkOTMzY2EwNGM4M2YwMWZmNjRkNjg2YjM4NmY2OWEyYjlmMGMzNmI1Yzg0NzdjZDJmMDY5NjMyZDZkOGQyY2VhYmJhNmQxNDhkMGIxMGRmNzc1MDRkY2QzZjc0NWI5NWFiMjM0NzcwMTdkMjgyOGU0NjE3NDc1MDlhMzE3ODIzYmU4YWZmMDI2NmQzZTI0ZTlhNGNiZDllYTFlZmFjOTA0ODNlNjBhYjczMzcwNzBlMWViNjY3OTI3Y2QyNTJhYjliMDJjNGMzY2M4OGMyZTc4ZDQzZTJlOTM1ZGEwN2EwNjJkOTRkNWE3MzY4YzgwOWU4NjhlMWFjYjU3NmZkMzEyZGRhZTE1Mjg3M2E3NDRjY2MxMDcxNDUyMWI3ZTIyMzU1ZmQ3NTgxNjlhMzcwMSIsIml0ZXJhdGlvbnMiOjk5OX0="
decrypted = encryption.decrypt(readable_string, nonce_value)
print(decrypted)
