ENCODING = 'ASCII'


def key_generator():
    for key in range(1, 256):
        yield key


def hack_xor_encrypted(message):
    bytes(message, encoding=ENCODING)
    for key in key_generator():
        decoded_bytes = bytes(byte ^ key for byte in message)
        result = decoded_bytes.decode(ENCODING, errors='ignore')
        if any(s.isalnum() for s in result.split()):
            print(result)


def encode_xor(text, key):
    text_bytes = bytes(text, ENCODING)
    key_code = ord(key)
    return bytes(byte ^ key_code for byte in text_bytes)


if __name__ == '__main__':
    message = 'Once upon a time...'
    encoded = encode_xor(message, 'a')
    hack_xor_encrypted(encoded)
