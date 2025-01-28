class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hash_map:
                return[hash_map[result],i]
            hash_map[nums[i]] = i  