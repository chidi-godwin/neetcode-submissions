from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if not len(s_count) == len(t_count):
            return False

        for letter, count in t_count.items():
            if not (count == s_count[letter]):
                return False
        return True