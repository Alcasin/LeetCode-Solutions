class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 1
        count = 1
        k = float("inf")
        i = 0
        j = 1
        while j<len(nums):
            if (nums[i]==nums[j]):
                nums[j] = k
                j+=1
            else:
                i=j
                j+=1
                count +=1
        nums.sort()
        return count
