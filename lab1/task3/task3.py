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


def try_decode(cipher, key_len):
    from string import printable
    char_sequences = split_text_to_char_sequences(CIPHER, KEY_LEN)
    for sequence in char_sequences[1:2]:
        key_to_chi_squared_statistics = {}
        for key in range(256):
            decoded_sequence = decode(sequence, chr(key))
            if not all(c in printable for c in decoded_sequence) or not all(c in (' ', *FREQUENCY_TABLE) for c in decoded_sequence):
                continue
            sequence_len = len(decoded_sequence)
            char_distribution = get_char_distribution(decoded_sequence)
            chi_squared = calculate_chi_squared(char_distribution, sequence_len)
            if len(sequence) != len(decoded_sequence):
                continue
            key_to_chi_squared_statistics[decoded_sequence] = chi_squared
        s = sorted(key_to_chi_squared_statistics.items(), key=lambda item: item[1])
        for i, statistics in s:
            print(i)
            print(statistics)


if __name__ == '__main__':
    try_decode(CIPHER, KEY_LEN)

    # k1 = (91, 123, 90, 122, 65, 97, 70)
    # k2 = (91, 123, 90, 122, 93, 125, 65)
    # k3 = (92, 124, 93, 125, 65, 97, 70)
    # k4 = (95, 127, 94, 126, 64, 96, 91)
    # k5 = (89, 121, 92, 124, 66, 98, 95)
    # k6 = (91, 123, 92, 124, 90, 122, 95)
    # res = []
    # for a in k1:
    #     for b in k2:
    #         for c in k3:
    #             for d in k4:
    #                 for e in k5:
    #                     for f in k6:
    #                         key = ''.join(chr(k) for k in (a, b, c, d, e, f))
    #                         decoded = decode(CIPHER, key).lower()
    #                         chi = calculate_chi_squared(get_char_distribution(decoded), len(decoded))
    #                         res.append((decoded, chi))
    # print(sorted(res, key=lambda i: (i[1][1], i[1][0]))[:3])
    # print(key)
    # decoded = decode(CIPHER, key).lower()
    # for s in range(KEY_LEN):
    #     print(decoded[s::KEY_LEN])
    # print(decoded)
    # example = "%$$  %$$ $$%%%$$$ $$$% $$%$%%$%%$%$%%%%$%%%% %$  $!  %$ $$%%$$$ %$ $$ $%% $%%$$% $$$%$%$ $$ %%% $$$$$$$$$$$$%\"$% %$%$%$ %$ $$%$$$% %$  $ $$$$%%u  $%$% $ $$$$%$$&%&&$&$'%!$!!&"
    # preformatted = preformat_sequence(example)
    # char_distribution = get_char_distribution(preformatted)
    # print(char_distribution)
    # print(calculate_chi_squared(char_distribution, len(preformatted)))
