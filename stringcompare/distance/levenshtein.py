import numpy as np
from stringcompare.distance.comparator import StringComparator


def levenshtein(s, t):
    m = len(s)
    n = len(t)
    buffer = np.arange(max(n, m) + 1)

    p = m
    for j in range(1, n + 1):
        temp = j - 1
        p = j
        for i in range(1, m + 1):
            p = min(p + 1, buffer[i] + 1, temp + (s[i - 1] != t[j - 1]))
            temp = buffer[i]
            buffer[i] = p
    return p


class Levenshtein(StringComparator):
    def __init__(self, normalize=True, similarity=False, dmat_size=100):
        self.normalize = normalize
        self.similarity = similarity

    def compare(self, s, t):
        size = len(s) + len(t)
        if size == 0:
            return 1 * self.similarity

        dist = levenshtein(s, t)
        if self.similarity:
            sim = (size - dist) / 2.0
            if self.normalize:
                sim = sim / (size - sim)
            return sim
        else:
            if self.normalize:
                dist = 2 * dist / (size + dist)
            return dist
