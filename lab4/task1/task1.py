import file_loaders
import random


def generate_passwords(amount):
    hundred_passwords_pool = file_loaders.load_list_file_into_mem('common_passwords_pool/hundred_passwords')
    million_passwords_pool = file_loaders.load_list_file_into_mem('common_passwords_pool/million_passwords')
    english_words_pool = file_loaders.load_list_file_into_mem('human_words_pool/english_words')
    russian_words_pool = file_loaders.load_list_file_into_mem('human_words_pool/russian_words')
    leetspeak_pool = file_loaders.load_dict_file_into_mem('leetspeak_pool/leetspeak')


generate_passwords(100)
corelation = {
        '5-10': 0,
        '50-90': 0,
        '1-5': 0,
        'rest': 0,
    }
percent_5_10 = tuple(percent for percent in range(1, 10+1))
percent_50_90 = tuple(percent for percent in range(1, 90+1))
percent_1_5 = tuple(percent for percent in range(1, 5+1))

password_amount = 1000000
for _ in range(password_amount):
    if random.randint(1, 100) in percent_5_10:
        corelation['5-10'] += 1

    elif random.randint(1, 100) in percent_50_90:
        corelation['50-90'] += 1

    elif random.randint(1, 100) in percent_1_5:
        corelation['1-5'] += 1
    else:
        corelation['rest'] += 1

print(corelation)