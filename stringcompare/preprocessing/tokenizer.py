from abc import ABC, abstractmethod
from .preprocessor import Preprocessor


class Tokenizer(ABC):
    """Abstract base class for string tokenization.

    The tokenize() method returns a Container with tokens extracted from a given string.
    """

    def __call__(self, sentence):
        return self.tokenize(sentence)

    @abstractmethod
    def tokenize(self, sentence):
        pass

    def batch_tokenize(self, sentences):
        return [self.tokenize(s) for s in sentences]


class DelimTokenizer(Tokenizer):
    def __init__(self, delim = " "):
        self.delim = delim

    def tokenize(self, sentence):
        return sentence.split(self.delim)


class WhitespaceTokenizer(DelimTokenizer):
    def __init__(self):
        super().__init__(delim=" ")


class NGram(Tokenizer):
    def __init__(self, n, preprocessor=None):
        self._validate_args(n, preprocessor)

        self.n = n
        self.level = "character"
        self.preprocessor = preprocessor

    def _validate_args(n, preprocessor):
        assert isinstance(n, int)
        assert isinstance(preprocessor, Preprocessor) or preprocessor is None

    def tokenize(self, sentence):
        if self.preprocessor:
            sentence = self.preprocessor(sentence)

        return zip(sentence[i:] for i in range(self.n))
