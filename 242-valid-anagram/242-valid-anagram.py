from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #created counter for each str to count occurences of each character
        s_counter = Counter(s)
        t_counter = Counter(t)
        #return comparison of counters
        return s_counter == t_counter
        