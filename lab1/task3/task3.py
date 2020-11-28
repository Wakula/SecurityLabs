CIPHER = '1c41023f564b2a130824570e6b47046b521f3f5208201318245e0e6b40022643072e13183e51183f5a1f3e4702245d4b285a1b23561965133f2413192e571e28564b3f5b0e6b50042643072e4b023f4a4b24554b3f5b0238130425564b3c564b3c5a0727131e38564b245d0732131e3b430e39500a38564b27561f3f5619381f4b385c4b3f5b0e6b580e32401b2a500e6b5a186b5c05274a4b79054a6b67046b540e3f131f235a186b5c052e13192254033f130a3e470426521f22500a275f126b4a043e131c225f076b431924510a295f126b5d0e2e574b3f5c4b3e400e6b400426564b385c193f13042d130c2e5d0e3f5a086b52072c5c192247032613433c5b02285b4b3c5c1920560f6b47032e13092e401f6b5f0a38474b32560a391a476b40022646072a470e2f130a255d0e2a5f0225544b24414b2c410a2f5a0e25474b2f56182856053f1d4b185619225c1e385f1267131c395a1f2e13023f13192254033f13052444476b4a043e131c225f076b5d0e2e574b22474b3f5c4b2f56082243032e414b3f5b0e6b5d0e33474b245d0e6b52186b440e275f456b710e2a414b225d4b265a052f1f4b3f5b0e395689cbaa186b5d046b401b2a500e381d4b23471f3b4051641c0f2450186554042454072e1d08245e442f5c083e5e0e2547442f1c5a0a64123c503e027e040c413428592406521a21420e184a2a32492072000228622e7f64467d512f0e7f0d1a'

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


def get_key_len(cipher):
    cipher_len = len(cipher)
    shifted_cipher = cipher
    key_len = 1
    for _ in range(cipher_len-1):
        shifted_cipher = shifted_cipher[-1] + shifted_cipher[:-1]
        matches = 0
        for c, shifted_c in zip(cipher, shifted_cipher):
            if c == shifted_c:
                matches += 1
        match_rate = matches / cipher_len
        if match_rate > RANDOM_COINCIDENCE_INDEX:
            key_len += 1
    return key_len

key = 'abc'

encoded = encode('Adventure travel Time for an adventure? Are you a bit bored with your nine-to-five routine? Have a look at our exciting range of holidays and decide what type of adventure youd like.Activity holidays Our activity holidays are for everyone, people who love danger or who just like sports. We have a huge variety of water, snow or desert holidays. Well take you SCUBA diving in the Red Sea or kayaking and white water rafting in Canada. If you prefer snow, you can try skiing or snowboarding in the Alps or even igloo-building. For those who like warmer weather, we also have sandboarding (the desert version of skateboarding) or camel safaris.Polar expeditions Take a cruise to Antarctica or the northern Arctic; explore a land of white natural beauty and wonderful wildlife. Our experts will explain everything about the two poles as you watch the penguins in Antarctica or whales and polar bears in the Arctic. Theres no greater adventure than travelling to the ends of the earth. A once-in-a-lifetime experience!Cultural journeys Our cultural journeys will help you discover ancient civilisations: India, Thailand, Egypt and many more. Visit temples, palaces and ancient ruins  just remember to bring your camera! Get to know local ways of life by exploring markets, trying exotic foods and meeting local people.', key=key)
print(get_key_len(encoded))
print(len(encoded))
# for i in s:
#     print(i)
