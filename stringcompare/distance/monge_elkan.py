from stringcompare.distance.comparator import StringComparator
from stringcompare.preprocessing.tokenizer import Tokenizer

from stringcompare.distance.levenshtein import Levenshtein
from stringcompare.preprocessing.tokenizer import WhitespaceTokenizer


class MongeElkan(StringComparator):
    def __init__(
        self,
        comparator: StringComparator = Levenshtein(),
        tokenizer: Tokenizer = WhitespaceTokenizer(),
        symmetrize=False,
    ):
        self.comparator = comparator
        self.tokenizer = tokenizer
        self.symmetrize = symmetrize

    def monge_elkan(self, s: str, t: str):
        s_tokens = self.tokenizer(s)
        t_tokens = self.tokenizer(t)

        return sum(min(self.comparator(i, j) for j in t_tokens) for i in s_tokens) / len(s_tokens)

    def compare(self, s: str, t: str):

        if self.symmetrize:
            return min(self.monge_elkan(s, t), self.monge_elkan(t, s))
        else:
            return self.monge_elkan(s, t)
