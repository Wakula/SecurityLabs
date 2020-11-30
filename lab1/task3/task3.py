from collections import defaultdict
from itertools import product
import math
# MAP IS COPY PASTED FROM http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
FREQUENCY_TABLE = {
    ' ': 13,
    'e': 12.02,
    't': 9.10,
    'a': 8.12,
    'o': 7.68,
    'i': 7.31,
    'n': 6.95,
    's': 6.28,
    'r': 6.02,
    'h': 5.92,
    'd': 4.32,
    'l': 3.98,
    # 'u': 2.88,
    # 'c': 2.71,
    # 'm': 2.61,
    # 'f': 2.30,
    # 'y': 2.11,
    # 'w': 2.09,
    # 'g': 2.03,
    # 'p': 1.82,
    # 'b': 1.49,
    # 'v': 1.11,
    # 'k': 0.69,
    # 'x': 0.17,
    # 'q': 0.11,
    # 'j': 0.10,
    # 'z': 0.07,
}

TRIGRAMS_DISTRIBUTION = {
    'the': 1.81,
    'and': 0.73,
    # 'tha': 0.33,
    'ent': 0.42,
    'ing': 0.72,
    'ion': 0.42,
    # 'tio': 0.31,
    # 'for': 0.34,
    # 'oft': 0.22,
    # 'sth': 0.21,
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


# Actually I just saw that in first several tries I get
# 0.04924242424242424
# 0.04734848484848485
# 0.05965909090909091
# 0.05397727272727273
# 0.04071969696969697
# 0.2178030303030303 <- this
# 0.052083333333333336
# 0.050189393939393936
# 0.05397727272727273
# 0.0625
# 0.038825757575757576
# 0.20833333333333334 < - this
# So I suggest that the key consists of 6 characters
# key_len = 6
KEY_LEN = 6


def get_characters_distribution(cipher, key_len):
    distribution = []
    for shift in range(key_len):
        char_sequence = cipher[shift::key_len]
        char_distribution = defaultdict(lambda: 0)
        for char in char_sequence:
            char_distribution[char] += 1
        max_char = max(char_distribution, key=lambda char: char_distribution[char])
        #char_distribution = {char: round(amount / len(char_sequence) * 100, 5) for char, amount in distribution.items()}
        distribution.append(max_char)
    return distribution


def create_key(distribution, permutation):
    return ''.join(chr(ord(char) ^ ord(swap_char)) for char, swap_char in zip(distribution, permutation))


def calculate_deviation(actual, required):
    return round(abs(required-actual) / required * 100)


def get_distribution_deviation(actual, required):
    deviation_sum = 0
    for trigram, distribution in required.items():
        deviation_sum += round(abs(distribution - actual.get(trigram, 0)) / distribution * 100)
    return deviation_sum / len(required)


deviations = defaultdict(lambda: 0)


def is_text(text):
    text = text.lower()
    words_sequence = ''.join(text.split())
    trigrams_distribution = defaultdict(lambda: 0)
    trigrams = []

    for char_index in range(len(words_sequence)):
        trigram = words_sequence[char_index:char_index+3]
        if len(trigram) == 3:
            trigrams.append(trigram)
    for trigram in trigrams:
        trigrams_distribution[trigram] += 1
    trigrams_distribution = {
        trigram: amount / len(words_sequence) * 100 for trigram, amount in trigrams_distribution.items()
        if trigram in TRIGRAMS_DISTRIBUTION
    }
    deviation = get_distribution_deviation(trigrams_distribution, TRIGRAMS_DISTRIBUTION)
    if deviation < 60:
        deviations[deviation] += 1
        print(deviations)
    return deviation


def try_decode(cipher, key_len):
    distribution = get_characters_distribution(CIPHER, KEY_LEN)
    print(distribution)
    # TODO: replace with FREQUENCY_TABLE
    l = FREQUENCY_TABLE
    tried_permutations = set()
    for permutation in product(l, repeat=key_len):
        if permutation in tried_permutations:
            continue
        tried_permutations.add(permutation)
        key = create_key(distribution, permutation)
        decoded = decode(cipher, key)
        decoded = is_text(decoded)
        if decoded < 60:
            print(permutation)


if __name__ == '__main__':
    try_decode(CIPHER, KEY_LEN)
