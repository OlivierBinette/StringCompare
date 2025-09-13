from stringcompare.distance.comparator import StringComparator
from itertools import zip_longest

def hamming(s, t):
    distance = 0
    for a, b in zip_longest(s, t):
        distance += (a != b)
    return distance

class Hamming(StringComparator):
    def __init__(self, normalize=True, similarity=False):
        self.similarity = similarity
        self.normalize = normalize

    def compare(self, s, t):
        length = max(len(s), len(t))
        if length == 0:
            return self.similarity
        
        result = hamming(s,t)

        if self.similarity:
            result = length - result
        if self.normalize:
            result /= length

        return result