from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import List


class Tokenizer(ABC):
    """Abstract base class for string tokenization.

    The tokenize() method returns a Container with tokens extracted from a given string.
    """

    def __call__(self, sentence: str) -> Collection:
        return self.tokenize(sentence)

    @abstractmethod
    def tokenize(self, sentence: str) -> Collection:
        pass

    def batch_tokenize(self, sentences: List[str]) -> List[Collection]:
        return [self.tokenize(s) for s in sentences]


class DelimTokenizer(Tokenizer):
    def __init__(self, delim: str = " "):
        self.delim = delim

    def tokenize(self, sentence: str) -> Collection:
        return sentence.split(self.delim)


class WhitespaceTokenizer(DelimTokenizer):
    def __init__(self):
        super().__init__(delim=" ")
