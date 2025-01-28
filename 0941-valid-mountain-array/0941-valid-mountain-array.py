class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        peak = False
        inc = True
        for i in range(1,len(arr)):
            if inc:
                if arr[i] > arr[i-1]:
                    continue
                elif arr[i] < arr[i-1]:
                    if i ==1:
                        return False
                    inc = False
                    peak = True
                else:
                    return False
            else:
                if arr[i] >= arr[i-1]:
                    return False
        return peak and not inc