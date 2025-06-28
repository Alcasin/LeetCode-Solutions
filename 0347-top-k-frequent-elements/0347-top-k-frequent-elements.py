class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for number in nums:
            if number in hmap:
                hmap[number] +=1
            else:
                hmap[number] =1
        sorted_values = sorted(hmap.items(),key = lambda x:x[1])
        return [item[0] for item in sorted_values[-k:]]