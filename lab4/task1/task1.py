import file_loaders
import password_generators
import random
import password_hashing
import csv_handler

HUNDRED_PASSWORDS_POOL_CHANCE = tuple(percent for percent in range(1, 10 + 1))
MILLION_PASSWORDS_POOL_CHANCE = tuple(percent for percent in range(1, 90 + 1))
RANDOM_PASSWORDS_PERCENT_CHANCE = tuple(percent for percent in range(1, 5 + 1))

ARGON_PASSWORDS_AMOUNT = 100000
SHA1_PASSWORDS_AMOUNT = 1000000
MDA5_PASSWORDS_AMOUNT = 1000000

ARGON_FILE = 'argon2i_passwords.csv'
MD5_FILE = 'mda5_passwords.csv'
SHA1_FILE = 'sha1_passwords.csv'


def generate_passwords(passwords_amount):
    hundred_passwords_pool = file_loaders.load_list_file_into_mem('common_passwords_pool/hundred_passwords')
    million_passwords_pool = file_loaders.load_list_file_into_mem('common_passwords_pool/million_passwords')
    human_password_factory = password_generators.HumanPasswordFactory()

    generated_passwords = []

    for _ in range(passwords_amount):
        if random.randint(1, 100) in RANDOM_PASSWORDS_PERCENT_CHANCE:
            generated_passwords.append(
                password_generators.generate_random_password()
            )
        elif random.randint(1, 100) in HUNDRED_PASSWORDS_POOL_CHANCE:
            generated_passwords.append(
                random.choice(hundred_passwords_pool)
            )
        elif random.randint(1, 100) in MILLION_PASSWORDS_POOL_CHANCE:
            generated_passwords.append(
                random.choice(million_passwords_pool)
            )
        else:
            generated_passwords.append(
                human_password_factory.create_password()
            )
    return generated_passwords


if __name__ == '__main__':
    argon_passwords = generate_passwords(ARGON_PASSWORDS_AMOUNT)
    mda5_passwords = generate_passwords(MDA5_PASSWORDS_AMOUNT)
    sha1_passwords = generate_passwords(SHA1_PASSWORDS_AMOUNT)

    csv_handler.export_to_csv(ARGON_FILE, password_hashing.create_argon2i_passwords(argon_passwords))
    csv_handler.export_to_csv(MD5_FILE, password_hashing.create_mda5_passwords(mda5_passwords))
    csv_handler.export_to_csv(SHA1_FILE, password_hashing.create_sha1_with_salt(sha1_passwords))
