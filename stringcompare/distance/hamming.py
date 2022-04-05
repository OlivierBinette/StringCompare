#hamming distance
from comparator import StringComparator

def hamming(s, t):
    if (len(s) != len(t)):
        raise ValueError("Words must be of the same size")
    distance = 0
    for i in range(0, len(t)):
        distance += (s[i] != t[i])
    return distance

class Hamming(StringComparator):
    def __init__(self, similarity=False):
        self.similarity = similarity

    def compare(self, s, t):
        l = len(s)
        distance = hamming(s,t)
        if self.similarity:
            return l - distance
        else:
            return distance
