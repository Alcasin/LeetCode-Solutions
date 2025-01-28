class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        j=0
        dif=len(nums1)-len(nums2)
        for i in range(dif,len(nums1)):
            nums1[i]=nums2[j]
            j=j+1
        nums1.sort()

        
       
            
        