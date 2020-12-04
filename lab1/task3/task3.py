from collections import defaultdict
from itertools import product
import math
# MAP IS COPY PASTED FROM http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
FREQUENCY_TABLE = {
    'e': 0.1202,
    't': 0.091,
    'a': 0.0812,
    'o': 0.0768,
    'i': 0.0731,
    'n': 0.0695,
    's': 0.0628,
    'r': 0.0602,
    'h': 0.0592,
    'd': 0.0432,
    'l': 0.0398,
    'u': 0.0288,
    'c': 0.0271,
    'm': 0.026,
    'f': 0.023,
    'y': 0.0211,
    'w': 0.0209,
    'g': 0.0203,
    'p': 0.0182,
    'b': 0.0149,
    'v': 0.0111,
    'k': 0.0069,
    'x': 0.0017,
    'q': 0.0011,
    'j': 0.001,
    'z': 0.0007
}


CIPHER = (
    '1c41023f564b2a130824570e6b47046b521f3f5208201318245e0e6b40022643072e13183e51183f5a1f3e4702245d4b285a1b235619'
    '65133f2413192e571e28564b3f5b0e6b50042643072e4b023f4a4b24554b3f5b0238130425564b3c564b3c5a0727131e38564b245d07'
    '32131e3b430e39500a38564b27561f3f5619381f4b385c4b3f5b0e6b580e32401b2a500e6b5a186b5c05274a4b79054a6b67046b540e'
    '3f131f235a186b5c052e13192254033f130a3e470426521f22500a275f126b4a043e131c225f076b431924510a295f126b5d0e2e574b'
    '3f5c4b3e400e6b400426564b385c193f13042d130c2e5d0e3f5a086b52072c5c192247032613433c5b02285b4b3c5c1920560f6b4703'
    '2e13092e401f6b5f0a38474b32560a391a476b40022646072a470e2f130a255d0e2a5f0225544b24414b2c410a2f5a0e25474b2f5618'
    '2856053f1d4b185619225c1e385f1267131c395a1f2e13023f13192254033f13052444476b4a043e131c225f076b5d0e2e574b22474'
    'b3f5c4b2f56082243032e414b3f5b0e6b5d0e33474b245d0e6b52186b440e275f456b710e2a414b225d4b265a052f1f4b3f5b0e3956'
    '89cbaa186b5d046b401b2a500e381d4b23471f3b4051641c0f2450186554042454072e1d08245e442f5c083e5e0e2547442f1c5a0a6'
    '4123c503e027e040c413428592406521a21420e184a2a32492072000228622e7f64467d512f0e7f0d1a'
)

CIPHER = ''.join(chr(int(CIPHER[i:i+2], base=16)) for i in range(0, len(CIPHER), 2))


def decode(message, key):
    def key_gen(key):
        while True:
            for c in key:
                yield ord(c)
    encoding_gen = key_gen(key)
    return ''.join(chr(ord(char) ^ next(encoding_gen)) for char in message)


def print_index_of_coincidence(cipher):
    cipher_len = len(cipher)
    shifted_cipher = cipher
    for _ in range(cipher_len-1):
        shifted_cipher = shifted_cipher[-1] + shifted_cipher[:-1]
        matches = 0
        for c, shifted_c in zip(cipher, shifted_cipher):
            if c == shifted_c:
                matches += 1
        match_rate = matches / cipher_len
        print(match_rate)


# Previous KEY_LEN = 6 appeared to be wrong because I did not know that original text was in Hex (TA ZA SHO???)
# (I had to get an advise to know that it is in Hex)
# After converting from Hex to bytes
# 0.0
# 0.0
# 0.058935361216730035  ->
# 0.0038022813688212928
# 0.0038022813688212928
# 0.049429657794676805  ->
# 0.0076045627376425855
# 0.0019011406844106464
# 0.08365019011406843   ->
# 0.0019011406844106464
# 0.0019011406844106464
# 0.06653992395437262   ->
# After converting to bytes i suggest that KEY_LEN is 3
KEY_LEN = 3


def get_char_distribution(char_sequence):
    char_distribution = defaultdict(lambda: 0)
    for char in char_sequence:
        char_distribution[char] += 1
    return char_distribution


def split_text_to_char_sequences(text, key_len):
    return tuple(text[shift::key_len] for shift in range(key_len))


def calculate_chi_squared(char_distribution: dict, char_sequence_len: int):
    chi_squared_sum = 0
    for char, distribution in FREQUENCY_TABLE.items():
        expected_char_amount = distribution * char_sequence_len
        actual_char_amount = char_distribution[char]
        chi_squared = (actual_char_amount - expected_char_amount) ** 2 / expected_char_amount
        chi_squared_sum += chi_squared
    return chi_squared_sum


def get_key(cipher, key_len):
    char_sequences = split_text_to_char_sequences(cipher, key_len)
    key = []
    for sequence in char_sequences:
        statistics = {}
        for key_part in range(256):
            decoded_sequence = decode(sequence, chr(key_part))
            if not decoded_sequence:
                continue
            sequence_len = len(decoded_sequence)
            char_distribution = get_char_distribution(decoded_sequence)
            chi_squared = calculate_chi_squared(char_distribution, sequence_len)
            statistics[key_part] = chi_squared
        key.append(min(statistics, key=lambda key_part: statistics[key_part]))
    return ''.join(chr(key_part) for key_part in key)


if __name__ == '__main__':
    # print_index_of_coincidence(CIPHER)
    key = get_key(CIPHER, KEY_LEN)
    print(decode(CIPHER, key))
