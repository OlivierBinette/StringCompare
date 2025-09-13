from stringcompare.distance.comparator import StringComparator


def jaro(s, t):
    if len(s) + len(t) == 0:
        return 1.0
    # Implementation is from https://rosettacode.org/wiki/Jaro_similarity#Python
    window = max(1, max(len(s), len(t)) // 2 - 1)
    m = 0
    found_s = len(s) * [False]
    found_t = len(t) * [False]
    for i, si in enumerate(s):
        for j, tj in enumerate(t):
            if (abs(i - j) < window) and (not found_t[j]) and si == tj:
                m = m + 1
                found_s[i] = True
                found_t[j] = True
                break

    if m == 0:
        return 0.0

    transpositions = 0
    j = 0
    for i, si in enumerate(s):
        if found_s[i]:
            while not found_t[j]:
                j = j + 1
            if s[i] != t[j]:
                transpositions += 1
            j = j + 1

    return (m / len(s) + m / len(t) + (m - transpositions / 2.0) / m) / 3.0


class Jaro(StringComparator):
    def __init__(self, similarity=False):
        self.similarity = similarity

    def compare(self, s, t):
        if self.similarity:
            return jaro(s, t)
        else:
            return 1.0 - jaro(s, t)
