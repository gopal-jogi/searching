import base64

def encode_to_base64_urlsafe(input_str):
    """
    Encodes a string to a Base64 URL-safe encoded string without padding.
    """
    # Convert the input string to bytes
    input_bytes = input_str.encode('utf-8')
    # Encode to Base64 URL-safe bytes
    base64_bytes = base64.urlsafe_b64encode(input_bytes)
    # Decode bytes to string and remove any padding '='
    base64_str = base64_bytes.decode('utf-8').rstrip('=')
    return base64_str

def decode_from_base64_urlsafe(base64_str):
    """
    Decodes a Base64 URL-safe encoded string back to the original data.
    """
    # Add padding if necessary
    padding_needed = (4 - len(base64_str) % 4) % 4
    base64_str_padded = base64_str + ('=' * padding_needed)
    # Decode from Base64 URL-safe
    decoded_bytes = base64.urlsafe_b64decode(base64_str_padded)
    return decoded_bytes  # Return the raw bytes

# Example usage:

# Encoded identifiers from the URLs (with prefix)
encoded_strings = [
    "__WweJMwQcq-VVvRkgfbgOMiVDr-ELM25adGTSbUrVU9M",
    "__5S4sgL1pSknebwwLBnEsVK89iVd6-INrZnzdBVEAjeA"
]

for encoded_str in encoded_strings:
    # Remove the prefix if present
    if encoded_str.startswith("__"):
        encoded_str = encoded_str[2:]

    # Decode the identifier
    decoded_data = decode_from_base64_urlsafe(encoded_str)

    # Since the decoded data may not be valid UTF-8 text, handle it appropriately
    # For example, print the hexadecimal representation
    hex_output = decoded_data.hex()
    print(f"Decoded data (hex) for '{encoded_str}':\n{hex_output}\n")
