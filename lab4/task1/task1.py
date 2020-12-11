import random
import sys
LAB4_DIR = '/home/rukadelica/PycharmProjects/SecurityLabs/lab4/task1/'
SECURITY_LABS_DIR = '/home/rukadelica/PycharmProjects/SecurityLabs/'

RANDOM_PASSWORD_MIN_LENGTH = 10
RANDOM_PASSWORD_MAX_LENGTH = 16
RANDOM_PASSWORD_SYMBOLS_POOL = 'abcdefghijklmnopqrstuvwxyz1234567890/?.,!@*%'

sys.path += [SECURITY_LABS_DIR, LAB4_DIR]


def load_file_into_mem(file_name):
    with open(f'{LAB4_DIR}{file_name}') as f:
        return tuple(line.strip() for line in f)


def generate_random_password(
        min_length=RANDOM_PASSWORD_MIN_LENGTH,
        max_length=RANDOM_PASSWORD_MAX_LENGTH,
        symbols_pool=RANDOM_PASSWORD_SYMBOLS_POOL
):
    length = random.randint(min_length, max_length+1)
    return ''.join(random.choice(symbols_pool) for _ in range(length))


def generate_human_password():
    pass


hundred_passwords_pool = load_file_into_mem('hundred_passwords_pool')
million_passwords_pool = load_file_into_mem('million_passwords_pool')
