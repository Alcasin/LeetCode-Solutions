class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = [1]
        rm = [1]
        result = [1] * len(nums)
        for i in range (1,len(nums)):
            lm.append(lm[i-1]*nums[i-1])
        for j in range (len(nums)-1,0,-1):
            rm.insert(0,rm[0]*nums[j])
        for k in range (len(nums)):
            result[k] = lm[k]*rm[k]
        return result

