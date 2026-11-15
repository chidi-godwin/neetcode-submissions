class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []

        for s in strs:
            sizes.append(str(len(s)))
        
        encoded = ','.join(sizes) + '#' + ''.join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []

        if not s:
            return []
        sizes = []
        i, j = 0,0

        while True:
            j += 1
            if (curr := s[j]) in (',', '#'):
                sizes.append(int(s[i:j]))
                if curr == '#':
                    break
                i = j = j + 1
        
        start = j + 1
        for size in sizes:
            end = start + size
            result.append(s[start: end])
            start = end
        return result
