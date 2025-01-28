class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)<2:
            return [-1]
        maxi = 0
        k=-1
        for i in range(len(arr)-1,-1,-1):
            if maxi>arr[i]:
                arr[i]=k
            else:
                maxi=arr[i]
                arr[i]=k
                k=maxi      
        return arr

            
            