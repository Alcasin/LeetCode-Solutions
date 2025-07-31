class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        answerset = set ()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            hash_map = {}
            target = -nums[i]
            for j in range(i+1,len(nums)):
                result = target - nums[j]
                if result in hash_map:
                    zero = tuple(sorted([nums[i], nums[j] , result]))
                    if zero not in answerset:
                        answerset.add(zero)
                        answer.append(list(zero))
                hash_map[nums[j]]=j
        return answer

