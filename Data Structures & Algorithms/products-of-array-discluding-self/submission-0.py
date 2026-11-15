class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)

        cumm = 1
        for i in range(len(nums)):
            pref[i] = cumm
            cumm *= nums[i]

        cumm = 1
        for i in range(len(nums) - 1, -1, -1):
            suff[i] = cumm
            cumm *= nums[i]

        result = []
        for left, right in zip(pref, suff):
            result.append(left * right)

        return result
        