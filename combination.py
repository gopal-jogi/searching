import base64
import json
import requests
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512
from pymongo import MongoClient

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

# Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
# db = client['easylead']  # DB name: 'easylead'
# urls_collection = db['urls']  # Collection name: 'urls'
# success_collection = db['success']  # Collection name: 'success'

# API request details
cookies = {
    'vtoken': '66fa390aad5834703730c7a5b9286848c6'
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    'DNT': '1',
    'Origin': 'chrome-extension://haphbbhhknaonfloinidkcmadhfjoghc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Session': '3e2742ffc8a01e387bc50f6402e91d4466f28a6e384491727171182',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'User-Token': 'eyJjaXBoZXJ0ZXh0IjoiTkJBTXhwQjB4RTg3UVg4UitOdkFIQzZvb2FuNlJEeUdzUmtma3BnMEYwcz0iLCJpdiI6IjUzYTZkMDFmOGYyMjNlNDJlZTNiYjY1YmE4NGVlMDdjIiwic2FsdCI6IjFlZjc1M2I3NmExMGQyMmM2ZWM0N2RjN2JmMDJjZDAwODk0MzQ4ZTViY2I1YWU0OTBkMDcxNDIzOTgxNGE0NDY4ZmMxY2ZhYzZlMTlmNzk3YjJkZDJkZjUzYTFhYTAyNjg4YjAwNGNiYTAwMjVmMTE4NDViMmY2MjlhYWJlY2I2MzU2OTI1ZmI1NmExZjQwOTE2YmY3NWMwMTA1MDQzMDI5MDFkYjU5NDAyZTM1MDgzNzI1OTIxNGY5Mzc1MGRhMzJlYTlmYTE0N2I0MTA0ZmJhZmZkYWFmYmY3ZmZmMWY2MGViNDg4MjIzZTcyYTZkNzE5YzBmZTZkYzlmNWI2ZmI5MzVhZjQ1OWFlYzg5ODlmY2FlNzVhYTQ5YWFhNzI2MmZiMmRmYWQyMDJlMWFiZjU5YzZiMDE3MjU4OTY4MzY0ZjUzY2YzZmZlZjA1ZGE3MjJhODQ1ZjdjMzY3NWMxY2YwMzg0YzNjMzU0MWI4NjU3MjQyODc5ODlkM2UyM2YzYWU0YmI0ZTdkNzRjMTkwNzg2MTkyOGFmYTYzMTNmMTg3ZjZlNTU3NDhiYmNiNjA4NDU4ZTgzMDFiM2ZjMTQ5NmIxOTMyNmM0NDY0ZjQ2NWRmNGY2MzI5MGQwYTllMDUyYzg2N2IyMzZiYjExYWFkNWIwNmU3NjFlNWMyNjBmMTZlIiwiaXRlcmF0aW9ucyI6OTk5fQ==',
    'sec-ch-ua': '"Google Chrome";v="128", "Not=A?Brand";v="8", "Chromium";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

encryption = Encryption()

# Loop through LinkedIn URLs in the 'urls' collection
urls_a = [
    "https://www.linkedin.com/in/ACwAAD7LxEMBWBpxt0bATWbOYHrY5lKzQdrq0Eo",
    "https://www.linkedin.com/in/nikhil-k-4039b4254",
    "https://www.linkedin.com/in/jagriti-jonwal-hr-8a7228221",
    "https://www.linkedin.com/in/abhinavkaul26"
]
print(len(urls_a))
listappend = []
for doc in urls_a:
    print(doc)
    ln_url = doc  # Retrieve LinkedIn URL
    nonce_value = 'mI4DwthFYmcefl7V'  # Nonce value for decryption

    if ln_url:
        # Prepare data for API request
        data = {
            'url': ln_url,
            'l': ln_url.split('/')[-1],  # Extract LinkedIn ID
            'trldata': '{}',
        }

        try:
            # Make POST request to EasyLeadz API
            response = requests.post('https://app.easyleadz.com/api/v5/show_email.php', cookies=cookies, headers=headers, data=data)
            response_data = response.json()
            print(response_data)
            if response_data.get('status') == '1' or response_data.get('status') == '0':
                # Get the encrypted data from the response
                encrypted_data = response_data['contactInfo']['pem']

                # Decrypt the email data
                decrypted_email = encryption.decrypt(encrypted_data, nonce_value)

                # Insert the decrypted email and LinkedIn URL into the 'success' collection
                listappend.append({
                    'ln_url': ln_url,
                    'email': decrypted_email
                })

                print(f"Successfully decrypted and stored email for {ln_url}")

        except Exception as e:
            print(f"Error processing {ln_url}: {e}")
print(listappend)
print("Process completed!")
