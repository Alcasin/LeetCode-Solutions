class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0 
        for i in range(len(nums)):
            if nums[k] == 0 and nums[i] != 0:
                nums[k],nums[i]=nums[i],nums[k]
                k += 1
            elif nums[k] != 0:
                k += 1
            
           