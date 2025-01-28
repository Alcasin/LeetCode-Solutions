class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        num_s = str(num)
        for i in num_s:
            if num%int(i)==0:
                counter+=1
        return counter