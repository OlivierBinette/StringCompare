from stringcompare.distance.jaro import jaro
from stringcompare.distance.comparator import StringComparator


def jarowinkler(s, t, p=0.1):
    ell = 0
    for i in range(min(4, len(s), len(t))):
        if s[i] == t[i]:
            ell = ell + 1
        else:
            break

    sim = jaro(s, t)

    return sim + ell * p * (1 - sim)


class JaroWinkler(StringComparator):
    def __init__(self, similarity=False):
        self.similarity = similarity

    def compare(self, s, t):
        if self.similarity:
            return jarowinkler(s, t)
        else:
            return 1.0 - jarowinkler(s, t)
