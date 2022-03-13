from collections import Collection
import itertools
from typing import List
from .tokenizer import Tokenizer
from .preprocessor import Preprocessor


class NGram(Tokenizer):
    def __init__(self, n, preprocessor=None):
        self._validate_args(n, preprocessor)

        self.n = n
        self.level = "character"
        self.preprocessor = preprocessor

    def _validate_args(n, preprocessor):
        assert isinstance(n, int)
        assert isinstance(preprocessor, Preprocessor) or preprocessor is None

    def tokenize(self, sentence: str) -> Collection:
        if self.preprocessor:
            sentence = self.preprocessor(sentence)

        return list(itertools.zip(sentence[i:] for i in range(self.n)))
