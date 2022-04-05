from comparator import StringComparator
from ..preprocessing.tokenizer import Tokenizer, WhitespaceTokenizer

def Jaccard(s,t, token):
  intersect = len(intersection(token(s), token(t)))
  union = len(token(s)) + len(token(t)) -  intersection
  return intersect / union
  

class Jaccard(StringComparator):
  def __init(self, similarity = False, tokenizer = WhitespaceTokenizer()):
    self.similarity = similarity
    self.token = tokenizer
    
  def compare(s,t,token):
    if similarity: 
      return Jaccard(s,t,token)
    else: 
      return 1 - Jaccard(s,t,token):

compartor = Jaccard()
print(comparator.compare("John", "Jane"))