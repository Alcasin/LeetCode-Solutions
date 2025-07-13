class Solution:
    def isPalindrome(self, s: str) -> bool:
        justnum = ''.join(i for i in s if i.isalnum())
        lowernum = justnum.lower()
        r = len(lowernum)-1
        i=0
        while i < r:
            if lowernum[i] != lowernum[r]:
                return False
            i+=1
            r-=1
        return True