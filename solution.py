from collections import defaultdict
import sys
def Smallest (S):
  count = len(set(list(S)))
  n = len(S)
  freq = defaultdict(int)
  idx = 0
  min_len = sys.maxsize
  distinct= 0 
  for j in range(n):
    freq[S[j]] += 1
    if freq[S[j]] == 1:
      distinct += 1
    
    if count == distinct:
      while freq[S[idx]] > 1:
        if freq[S[idx]] > 1:
          freq[S[idx]] -= 1
        idx += 1
      
      curr_len = j - idx + 1
      min_len = min(min_len, curr_len)
  return min_len
 
S = input()
t_ = Smallest(S)
print (t_)