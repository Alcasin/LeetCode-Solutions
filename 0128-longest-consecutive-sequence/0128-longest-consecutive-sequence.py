class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        slist = sorted(nums)
        count = 1
        answer = 1
        for i in range (len(slist)-1):
            if slist[i] +1 ==slist[i+1]:
                count +=1
                if count > answer:
                    answer = count
            elif slist[i] ==slist[i+1]:
                continue
            else:
                count = 1
        if len(nums) == 0:
            return 0
        return answer
