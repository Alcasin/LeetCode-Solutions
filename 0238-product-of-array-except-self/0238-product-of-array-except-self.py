class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = 1
        rm = 1
        result = [1] * len(nums)
        for i in range (len(nums)):
            result[i] = lm
            lm *= nums[i]
        for j in range (len(nums)-1,-1,-1):
            result[j] *= rm
            rm *= nums[j]
        return result

