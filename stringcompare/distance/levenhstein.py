import numpy as np
from .comparator import StringComparator


def levenshtein(s, t, dmat):
    m = len(s)
    n = len(t)
    dmat[:, 0] = np.arange(dmat.shape[0])

    for j in range(1, n+1):
        dmat[0, (j-1) % 2] = j-1
        dmat[0, j % 2] = j
        for i in range(1, m+1):
            cost = 0
            if s[i-1] != t[j-1]:
                cost = 1
            dmat[i, j % 2] = min(dmat[i-1, j % 2] + 1, dmat[i, (j-1) % 2] +
                                 1, dmat[i-1, (j-1) % 2] + cost)
    return dmat[m, n % 2]


class Levenshtein(StringComparator):

    def __init__(self, normalize=True, similarity=False, dmat_size=100):
        self.dmat = np.zeros((dmat_size, 2))
        self.normalize = normalize
        self.similarity = similarity

    def compare(self, s1, s2):
        dist = levenshtein(s1, s2, self.dmat)
        if self.similarity:
            sim = (len(s1) + len(s2) - dist) / 2.0
            if self.normalize:
                sim = sim / (len(s1) + len(s2) - sim)
            return sim
        else:
            if self.normalize:
                dist = 2 * dist / (len(s1) + len(s2) + dist)
            return dist
