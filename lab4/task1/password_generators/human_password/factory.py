from collections import namedtuple
import random

import file_loaders
from password_generators.human_password import strategies

MAX_WORDS = 2
MIN_WORDS = 1

ENGLISH_WORDS_POOL = file_loaders.load_list_file_into_mem('human_words_pool/english_words')
RUSSIAN_WORDS_POOL = file_loaders.load_list_file_into_mem('human_words_pool/russian_words')
LEETSPEAK_POOL = file_loaders.load_dict_file_into_mem('leetspeak_pool/leetspeak')


PasswordStrategyOptions = namedtuple('PasswordStrategy', ['strategy_cls', 'words_pool', 'kwargs'])


class HumanPasswordFactory:
    password_strategies = (
        PasswordStrategyOptions(
            strategies.EnglishPasswordBuilder,
            ENGLISH_WORDS_POOL,
            {'leetspeak_pool': LEETSPEAK_POOL},
        ),
        PasswordStrategyOptions(
            strategies.RussianPasswordBuilder,
            RUSSIAN_WORDS_POOL,
            {},
        ),
    )

    def __init__(self, min_words=MIN_WORDS, max_words=MAX_WORDS):
        self.min_words = min_words
        self.max_words = max_words

    def create_password(self):
        strategy_options = random.choice(self.password_strategies)
        strategy = strategy_options.strategy_cls(
            strategy_options.words_pool,
            self.min_words,
            self.max_words,
            **strategy_options.kwargs,
        )
        strategy.build()
        return strategy.password
