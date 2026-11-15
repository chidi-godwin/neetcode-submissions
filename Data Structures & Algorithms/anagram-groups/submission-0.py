from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        def hash(word):
            return "".join(sorted(word))

        for word in strs:
            key = hash(word)
            result[key].append(word)

        return list(result.values())