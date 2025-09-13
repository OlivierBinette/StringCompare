from typing import Counter
import numpy as np
from stringcompare.distance.comparator import StringComparator


def _character_difference(s, t):
    s = Counter(s)
    t = Counter(t)
    
    return sum(s.values()) + sum(t.values()) - 2 * sum((s&t).values())

class CharacterDifference(StringComparator):
    def __init__(self, normalize=True, similarity=False):
        self.normalize = normalize
        self.similarity = similarity

    def compare(self, s, t):
        size = len(s) + len(t)
        if size == 0:
            return 1 * self.similarity

        dist = _character_difference(s, t)
        if self.similarity:
            sim = (size - dist) / 2.0
            if self.normalize:
                sim = sim / (size - sim)
            return sim
        else:
            if self.normalize:
                dist = 2 * dist / (size + dist)
            return dist
