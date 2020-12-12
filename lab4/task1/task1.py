import file_loaders
import password_generators
import random

HUNDRED_PASSWORDS_POOL_CHANCE = tuple(percent for percent in range(1, 10 + 1))
MILLION_PASSWORDS_POOL_CHANCE = tuple(percent for percent in range(1, 90 + 1))
RANDOM_PASSWORDS_PERCENT_CHANCE = tuple(percent for percent in range(1, 5 + 1))


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

generate_passwords(1000000)
print('Done')
