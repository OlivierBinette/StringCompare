from abc import ABC, abstractmethod

class Tokenizer(ABC):
    """String tokenization interface."""

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


class NGramTokenizer(Tokenizer):
    # TODO: Add "delim" option to tokenize around words or other delimiters. delim="" should tokenize at the character level.
    def __init__(self, n):

        self.n = n

    def tokenize(self, sentence):
        return [sentence[i:i+self.n] for i in range(len(sentence)-self.n+1)]
