#hamming distance
from comparator import StringComparator

def hamming(s, t):
    t_len = len(t)
    s_len = len(s)
    small_len = min(t_len,s_len)
    large_len = max(t_len, s_len)
    distance = 0 
    for i in range(0, small_len):
        distance += (s[i] != t[i])
    return distance + large_len - small_len

class Hamming(StringComparator):
    def __init__(self, similarity=False):
        self.similarity = similarity

    def compare(self, s, t):
        l = max(len(s), len(t))
        distance = hamming(s,t)
        if self.similarity:
            return l - distance
        else:
            return distance

