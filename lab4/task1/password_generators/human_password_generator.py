import random


class AbstractPasswordBuilder:
    def __init__(self, words_pool, min_length, max_length):
        length = random.randint(min_length, max_length)
        self.password = ''.join(random.choice(words_pool) for _ in range(length)).lower()

    def maybe_change_some_letters_to_upper(self):
        pass

    def build(self):
        raise NotImplementedError


class EnglishPasswordBuilder:
    def __init__(self, words_pool, min_length, max_length):
        length = random.randint(min_length, max_length+1)
        self.password = ''.join(random.choice(words_pool) for _ in range(length)).lower()

    def maybe_change_some_letters_to_leetspeek(self):
        pass

    def build(self):
        pass


class RussianPasswordBuilder:
    QWERTY_MAP = {
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
        'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
        'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.'
    }
    ENGLISH_LETTERS_MAP = {
        'й': 'j', 'ц': 'c', 'у': 'u', 'к': 'k', 'е': 'e', 'н': 'n', 'г': 'g', 'ш': 'sh', 'щ': 'sch', 'з': 'z',
        'х': 'h', 'ф': 'f', 'ы': 'y', 'в': 'v', 'а': 'a', 'п': 'p', 'р': 'r', 'о': 'o', 'л': 'l', 'д': 'd',
        'ж': 'j', 'э': "e", 'я': 'ja', 'ч': 'ch', 'с': 'c', 'м': 'm', 'и': 'i', 'т': 't', 'б': 'b', 'ю': 'ju'
    }

    def maybe_change_all_letters_to_english(self):
        pass

    def maybe_change_all_to_qwerty(self):
        pass

    def build(self):
        pass
