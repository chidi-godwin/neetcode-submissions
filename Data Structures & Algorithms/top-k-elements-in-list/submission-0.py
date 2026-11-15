from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        output = []
        heap = []

        for key, freq in counter.items():
            if len(heap) < len(counter) - k:
                heapq.heappush(heap, (-freq, key))
            else:
                output.append(heapq.heappushpop(heap, (-freq, key))[-1])

        return output


