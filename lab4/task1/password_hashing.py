import hashlib
from nacl.pwhash import argon2i


ENCODING = 'utf-8'
SHA1_SALT_LENGTH = 128


def generate_random(csprng_source, bits):
    bytes_amount = bits // 8
    with(open(csprng_source, 'rb')) as f:
        return bytes(f.read(bytes_amount))


def generate_nonce(bits):
    return generate_random('/dev/urandom', bits)


def create_sha1_with_salt(passwords):
    hashed = []
    for password in passwords:
        salt = generate_nonce(SHA1_SALT_LENGTH)
        password_bytes = password.encode(ENCODING)
        password_hex = hashlib.sha1(password_bytes+salt).hexdigest()
        salt_hex = salt.hex()
        hashed.append(f'salt={salt_hex}$hash={password_hex}')
    return hashed


def create_mda5_passwords(passwords):
    return [hashlib.md5(password.encode(ENCODING)).hexdigest() for password in passwords]


def create_argon2i_passwords(passwords):
    hashed = []
    for password in passwords:
        argon_hash = argon2i.str(password.encode(ENCODING))
        data = argon_hash.split(b'$')
        salt_hex = data[4].decode('ascii')
        password_hex = data[5].decode('ascii')
        hashed.append(f'salt={salt_hex}$hash={password_hex}')
    return hashed
