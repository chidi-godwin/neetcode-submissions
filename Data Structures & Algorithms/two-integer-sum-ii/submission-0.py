class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(numbers):
            diff = target - num
            
            if diff in diffs:
                return [diffs[diff] + 1, i + 1]
            
            diffs[num] = i