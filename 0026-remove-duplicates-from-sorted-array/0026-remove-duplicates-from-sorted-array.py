class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val=-101
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                val=nums[k]
                k+=1
        return k