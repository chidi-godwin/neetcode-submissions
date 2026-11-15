from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        def countfreq(word):
            counter = [0] * 26
            offset = ord('a')

            for letter in word:
                i = ord(letter) - offset
                counter[i] += 1

            return tuple(counter)

        for word in strs:
            key = countfreq(word)
            result[key].append(word)

        return list(result.values())