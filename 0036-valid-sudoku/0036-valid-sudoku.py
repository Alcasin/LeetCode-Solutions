class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            exist = set()           
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in exist:
                        return False
                    exist.add(num)
        for j in range(9):
            exist = set()           
            for i in range(9):
                num = board[i][j]
                if num != ".":
                    if num in exist:
                        return False
                    exist.add(num)

        for a in range(0,7,3):
            for b in range(0,7,3):
                exist = set()
                for i in range(a,a+3):
                    for j in range(b,b+3):
                        num = board[i][j]
                        if num != ".":
                            if num in exist:
                                return False
                            exist.add(num)
        return True
        