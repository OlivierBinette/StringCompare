from .comparator import StringComparator
from ..preprocessing.tokenizer import Tokenizer, WhitespaceTokenizer

def jaccard(s,t,token):
  s_token = token(s) 
  t_token = token(t)
  intersection = [value for value in s_token if value in t_token]
  len_intersection = len(intersection)
  return len_intersection/(len(s_token) + len(t_token) - len_intersection)
  
class Jaccard(StringComparator):
  def __init__(self, similarity = True, tokenizer = WhitespaceTokenizer()):
    self.similarity = similarity
    self.tokenizer = tokenizer 

  def compare(self, s, t):
    if self.similarity: 
      return jaccard(s,t,self.tokenizer)
    else:
      return 1 - jaccard(s,t,self.tokenizer)


  