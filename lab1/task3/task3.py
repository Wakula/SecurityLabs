from collections import defaultdict

# MAP IS COPY PASTED FROM http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
FREQUENCY_TABLE = {
    'E': 12.02,
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 7.31,
    'N': 6.95,
    'S': 6.28,
    'R': 6.02,
    'H': 5.92,
    'D': 4.32,
    'L': 3.98,
    'U': 2.88,
    'C': 2.71,
    'M': 2.61,
    'F': 2.30,
    'Y': 2.11,
    'W': 2.09,
    'G': 2.03,
    'P': 1.82,
    'B': 1.49,
    'V': 1.11,
    'K': 0.69,
    'X': 0.17,
    'Q': 0.11,
    'J': 0.10,
    'Z': 0.07,
}

F1 = '1' # 46 !
F2 = '2' # 28 !
F3 = '3' # 17
F4 = '4' # 16
F5 = '5' # 15 !
F6 = '6'
F7 = '7' # 53 !
F8 = '8'
F9 = '9'
F10 = 'A'
F11 = 'B' # 10 !
F12 = 'C'
F13 = 'D' # 24 !
F14 = 'E' # 21 !
F15 = 'F' # 18 !
F16 = 'G' # 17 !

sequence1_frequency = {
    '2': F1,  # 46.023
    '3': F2,  # 28.977
    '6': F3,  # 17.045

    '0': 'u',  # 2.841
    # TODO: try swap 'c' and 'm'
    '1': 'c',  # 2.273
    '7': 'm',  # 2.273

    'c':  'k',  # 0.568
}
sequence2_frequency = {
    'b': F4,  # 16.477,
    'f': F5,  # 15.341,
    'e': F6,  # 11.364,

    '8': "*",#'t',  # 9.659,
    '2': "*",#'a',  # 9.091,
    '4': "*",#'o',  # 7.955,
    'c': "*",#'r',  # 5.114,
    'a': "*",#'h',  # 4.545,
    '6': "*",#'d',  # 4.545,
    '5': "*",#'l',  # 3.977,
    '7': "*",#'u',  # 3.409,
    '9': "*",#'c',  # 3.409,
    '3': "*",#'f',  # 2.273,
    '0': "*",#'b',  # 1.136,
    'd': "*",#'v',  # 1.136,
    '1': "*",#'k',  # 0.568
}
sequence3_frequency = {
    '5': F7,  # 53.143,
    '4': F8,  # 24.0,
    '1': F9,  # 17.143,

    '6': "*",#'f',  # 2.286,
    '7': "*",#'p',  # 1.714,
    '0': "*",#'v',  # 1.143,
    'a': "*",#'k',  # 0.571
}
sequence4_frequency = {
    '3': F10,  # 15.429,
    '6': F11,  # 10.286,

    '7': "*",#'t',  # 9.714,
    '0': "*",#'a',  # 9.143,
    'a': "*",#'o',  # 9.143,
    'd': "*",#'i',  # 7.429,
    'c': "*",#'n',  # 6.857,
    'f': "*",#'s',  # 6.286,
    '1': "*",#'r',  # 5.714,
    '4': "*",#'h',  # 5.714,
    '2': '*',  # 4.571,
    'b': '*',  # 4.571,
    'e': '*',  # 2.286,
    '5': '*',  # 1.143,
    '9': '*',  # 1.143,
    '8': '*',  # 0.571
}
sequence5_frequency = {
    '0': F12,  # 48.0,
    '1': F13,  # 24.0,
    '4': F14,  # 21.714,

    '2': '*',  # 2.857,
    '3': '*',  # 1.714,
    '5': '*',  # 1.143,
    '8': '*',  # 0.571
}
sequence6_frequency = {
    'b': F15,  # 18.857,
    'e': F16,  # 17.143,

    '4': '*',  # 9.143,
    '8': '*',  # 8.571,
    '2': '*',  # 8.0,
    'f': '*',  # 6.857,
    '9': '*',  # 6.857,
    'a': '*',  # 6.857,
    '7': '*',  # 6.286,
    '5': '*',  # 3.429,
    '3': '*',  # 3.429,
    'c': '*',  # 2.286,
    '1': '*',  # 0.571,
    '0': '*',  # 0.571,
    '6': '*',  # 0.571,
    'd': '*',  # 0.571
}

character_swap_maps = (
    sequence1_frequency,
    sequence2_frequency,
    sequence3_frequency,
    sequence4_frequency,
    sequence5_frequency,
    sequence6_frequency
)


def raise_error_if_not_unique_characters(seq):
    seq = {k: v for k, v in seq.items() if v != '*'}
    if len(seq) != len(set(seq.values())):
        raise Exception


raise_error_if_not_unique_characters(sequence1_frequency)
raise_error_if_not_unique_characters(sequence2_frequency)
raise_error_if_not_unique_characters(sequence3_frequency)
raise_error_if_not_unique_characters(sequence4_frequency)
raise_error_if_not_unique_characters(sequence5_frequency)
raise_error_if_not_unique_characters(sequence6_frequency)


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

RANDOM_COINCIDENCE_INDEX = 1 / 26


def encode(message, key):
    def key_gen(key):
        key_bytes = bytes(key, 'ASCII')
        while True:
            for c in key_bytes:
                yield c

    encoding_gen = key_gen(key)
    message_bytes = bytes(message, 'ASCII')
    return bytes(byte ^ next(encoding_gen) for byte in message_bytes).decode('utf-8')


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
# And thus key_len is len(CIPHER) / 6
characters_in_key = 6
key_len = len(CIPHER) / characters_in_key

swapped_sequences = []
for shift in range(characters_in_key):

    sequence = CIPHER[shift::characters_in_key]
    mapping = defaultdict(lambda: 0)

    for char in sequence:
        mapping[char] += 1

    mapping = dict(sorted(mapping.items(), key=lambda char_amount: char_amount[1], reverse=True))
    # print({char: round(amount / len(sequence) * 100, 3) for char, amount in mapping.items()})
    ordered_sequence_characters = tuple(mapping)
    frequency_characters = tuple(FREQUENCY_TABLE)

    swapped_sequences.append(''.join(character_swap_maps[shift][char] for char in sequence))
decoded = ''.join(''.join(swapped_characters) for swapped_characters in zip(*swapped_sequences))
print(decoded)

# encoded = encode(
#     'Adventure travel Time for an adventure? Are you a bit bored with your nine-to-five routine? Have a look at our exciting range of holidays and decide what type of adventure youd like.Activity holidays Our activity holidays are for everyone, people who love danger or who just like sports. We have a huge variety of water, snow or desert holidays. Well take you SCUBA diving in the Red Sea or kayaking and white water rafting in Canada. If you prefer snow, you can try skiing or snowboarding in the Alps or even igloo-building. For those who like warmer weather, we also have sandboarding (the desert version of skateboarding) or camel safaris.Polar expeditions Take a cruise to Antarctica or the northern Arctic; explore a land of white natural beauty and wonderful wildlife. Our experts will explain everything about the two poles as you watch the penguins in Antarctica or whales and polar bears in the Arctic. Theres no greater adventure than travelling to the ends of the earth. A once-in-a-lifetime experience!Cultural journeys Our cultural journeys will help you discover ancient civilisations: India, Thailand, Egypt and many more. Visit temples, palaces and ancient ruins  just remember to bring your camera! Get to know local ways of life by exploring markets, trying exotic foods and meeting local people.',
#     key=key
# )
