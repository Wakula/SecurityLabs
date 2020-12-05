from collections import defaultdict


CIPHER1 = 'ad924af7a9cdaf3a1bb0c3fe1a20a3f367d82b0f05f8e75643ba688ea2ce8ec88f4762fbe93b50bf5138c7b699'
CIPHER2 = 'a59a0eaeb4d1fc325ab797b31425e6bc66d36e5b18efe8060cb32edeaad68180db4979ede43856a24c7d'
CIPHER3 = 'a59a0eaeaad7fc3c56fe82fd1f6bb5a769c43a0f0cfae74f0df56fdae3db8d9d840875ecae2557bf563fcea2'
CIPHER4 = 'a59a0eaea8ddf93c08fe81e11e2ab2bb6d962f0f1af2f44243b46cc1b6d6c291995d65a9a5234aa204'
CIPHER5 = 'ad924af7a9cdaf3a1bb0c3f51439a5b628cf215a1fbdee4302a77a8ea2cc86c8984d65ffac6c58bf5b71dab8841136'
CIPHER6 = 'b09b4afda3caf93c5aa78ce6096bb2a67ad86e4302f3e10602b37acbb1829680935137e8bb2919b6503fccfdca5461'
CIPHER7 = 'a59a0eaeb5d7af3115b287b31425e6a460d3200f19f5e35406f567dde3cc8d9c9e4179eee92557f1463edc'
CIPHER8 = 'a18c09ebb6ccaf2d12bbc3c41227aaf37fde274c05bdf5471aa62edaac82968093452da9eb0456bd5b71c6bfcb56'


def from_hex_to_str(cipher):
    return ''.join(chr(int(cipher[i:i + 2], base=16)) for i in range(0, len(cipher), 2))


def xor_each(cipher1, cipher2):
    # return ''.join(chr(ord(char1) ^ ord(char2)) for char1, char2 in zip(cipher1, cipher2))
    return tuple((ord(char1) ^ ord(char2)) for char1, char2 in zip(cipher1, cipher2))


CIPHER_TEST_1 = from_hex_to_str(CIPHER1)
CIPHER_TEST_2 = from_hex_to_str(CIPHER2)
CIPHER_TEST_3 = from_hex_to_str(CIPHER3)
CIPHER_TEST_4 = from_hex_to_str(CIPHER4)
CIPHER_TEST_5 = from_hex_to_str(CIPHER5)
CIPHER_TEST_6 = from_hex_to_str(CIPHER6)
CIPHER_TEST_7 = from_hex_to_str(CIPHER7)
CIPHER_TEST_8 = from_hex_to_str(CIPHER8)

CIPHERS = [
    CIPHER_TEST_1, CIPHER_TEST_2, CIPHER_TEST_3, CIPHER_TEST_4,
    CIPHER_TEST_5, CIPHER_TEST_6, CIPHER_TEST_7, CIPHER_TEST_8
]
# for i in (CIPHER_TEST_2, CIPHER_TEST_3,CIPHER_TEST_4, CIPHER_TEST_5,CIPHER_TEST_6, CIPHER_TEST_7, CIPHER_TEST_8):
#     print(xor_each(CIPHER_TEST_1, i))
suggested_key = defaultdict(set)


for cipher in CIPHERS:
    ciphers_to_xor = [c for c in CIPHERS if c != cipher]
    for i in range(len(ciphers_to_xor) - 1):
        xor1 = xor_each(cipher, ciphers_to_xor[i])
        xor2 = xor_each(cipher, ciphers_to_xor[i+1])
        for (char_pos, (i, j)) in enumerate(zip(xor1, xor2)):
            space = ' '
            if i >= 65 and j >= 65:
                key_part = i ^ ord(space)
                suggested_key[char_pos].add(key_part)

print(suggested_key)
