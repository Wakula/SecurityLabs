import random


RANDOM_PASSWORD_MIN_LENGTH = 10
RANDOM_PASSWORD_MAX_LENGTH = 16
RANDOM_PASSWORD_SYMBOLS_POOL = 'abcdefghijklmnopqrstuvwxyz1234567890/?.,!@*%'


def generate_random_password(
        min_length=RANDOM_PASSWORD_MIN_LENGTH,
        max_length=RANDOM_PASSWORD_MAX_LENGTH,
        symbols_pool=RANDOM_PASSWORD_SYMBOLS_POOL
):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(symbols_pool) for _ in range(length))
