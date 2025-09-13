from stringcompare.distance.comparator import StringComparator
import numpy as np


def lcs(s, t, dmat):
    m = len(s)
    n = len(t)
    dmat = np.zeros(m + 1)

    p = 0
    for j in range(1, n + 1):
        temp = 0
        p = 0
        for i in range(1, m + 1):
            if s[i - 1] != t[j - 1]:
                p = max(dmat[i], p)
            else:
                p = temp + 1
            temp = dmat[i]
            dmat[i] = p

    return p


class LCSDistance(StringComparator):
    def __init__(self, normalize=True, similarity=False, dmat_size=100):
        self.dmat = np.zeros(dmat_size)
        self.normalize = normalize
        self.similarity = similarity

    def compare(self, s, t):
        size = len(s) + len(t)
        if size == 0:
            return 1 * self.similarity

        dist = size - 2 * lcs(s, t, self.dmat)
        if self.similarity:
            sim = (size - dist) / 2.0
            if self.normalize:
                sim = sim / (size - sim)
            return sim
        else:
            if self.normalize:
                dist = 2 * dist / (size + dist)
            return dist
