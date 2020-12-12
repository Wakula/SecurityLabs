import random


def coin_flip() -> bool:
    return random.choice((True, False))


class AbstractPasswordStrategy:
    def __init__(self, words_pool, min_words, max_words, **kwargs):
        amount = random.randint(min_words, max_words)
        self.password = ''.join(random.choice(words_pool) for _ in range(amount)).lower()

    def maybe_change_some_letters_to_upper(self):
        if coin_flip():
            return
        self.password = ''.join(char if coin_flip() else char.upper() for char in self.password)

    def build(self):
        raise NotImplementedError


class EnglishPasswordBuilder(AbstractPasswordStrategy):
    def __init__(self, words_pool, min_words, max_words, **kwargs):
        self.leetspeak_pool = kwargs.pop('leetspeak_pool')
        super().__init__(words_pool, min_words, max_words, **kwargs)

    def maybe_change_some_letters_to_leetspeek(self):
        available_swaps = tuple(sequence for sequence in self.leetspeak_pool if sequence in self.password)
        while coin_flip():
            sequence_to_swap = random.choice(available_swaps)
            choice = random.choice(self.leetspeak_pool[sequence_to_swap])
            self.password = self.password.replace(sequence_to_swap, choice)

    def build(self):
        self.maybe_change_some_letters_to_leetspeek()
        self.maybe_change_some_letters_to_upper()


class RussianPasswordBuilder(AbstractPasswordStrategy):
    QWERTY_MAP = {
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
        'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
        'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
        'ё': '`',
    }
    ENGLISH_LETTERS_MAP = {
        'й': 'j', 'ц': 'c', 'у': 'u', 'к': 'k', 'е': 'e', 'н': 'n', 'г': 'g', 'ш': 'sh', 'щ': 'sch', 'з': 'z',
        'х': 'h', 'ф': 'f', 'ы': 'y', 'в': 'v', 'а': 'a', 'п': 'p', 'р': 'r', 'о': 'o', 'л': 'l', 'д': 'd',
        'ж': 'j', 'э': "e", 'я': 'ja', 'ч': 'ch', 'с': 'c', 'м': 'm', 'и': 'i', 'т': 't', 'б': 'b', 'ю': 'ju',
        'ё': 'e',
    }

    def change_all_letters_to_english(self):
        self.password = ''.join(self.ENGLISH_LETTERS_MAP.get(letter, '') for letter in self.password)

    def change_all_to_qwerty(self):
        self.password = ''.join(self.QWERTY_MAP.get(letter, '') for letter in self.password)

    def build(self):
        if coin_flip():
            self.change_all_letters_to_english()
        elif coin_flip():
            self.change_all_to_qwerty()
        self.maybe_change_some_letters_to_upper()
