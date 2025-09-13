import numpy as np
from stringcompare.distance.comparator import StringComparator


def dameraulevenshtein(s, t, dmat):
    # Algorithm is described at https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    m = len(s)
    n = len(t)
    dmat[:, 0] = np.arange(dmat.shape[0])

    for j in range(1, n + 1):
        dmat[0, (j - 1) % 2] = j - 1
        dmat[0, j % 3] = j
        for i in range(1, m + 1):
            cost = 0
            if s[i - 1] != t[j - 1]:
                cost = 1
            dmat[i, j % 3] = min(
                dmat[i - 1, j % 3] + 1,
                dmat[i, (j - 1) % 3] + 1,
                dmat[i - 1, (j - 1) % 3] + cost,
            )
            if i > 1 and j > 1 and s[i - 1] == t[j - 2] and s[i - 2] == t[j - 1]:
                dmat[i, j % 3] = min(dmat[i, j % 3], dmat[i - 2, (j - 2) % 3] + 1)

    return dmat[m, n % 3]


class DamerauLevenshtein(StringComparator):
    def __init__(self, normalize=True, similarity=False, dmat_size=100):
        self.dmat = np.zeros((dmat_size, 3))
        self.normalize = normalize
        self.similarity = similarity

    def compare(self, s, t):
        ssize = len(s) + len(t)
        if ssize == 0:
            return 1 * self.similarity

        dist = dameraulevenshtein(s, t, self.dmat)
        if self.similarity:
            sim = (ssize - dist) / 2.0
            if self.normalize:
                sim = sim / (ssize - sim)
            return sim
        else:
            if self.normalize:
                dist = 2 * dist / (ssize + dist)
            return dist
