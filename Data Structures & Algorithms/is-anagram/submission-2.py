class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = Counter(s)
        dict_2 = Counter(t)
        return dict_1 == dict_2
            
   
        
 