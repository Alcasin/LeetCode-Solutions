class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "{":
                stack.append("{")
            elif p == "[":
                stack.append("[")
            elif p == "(":
                stack.append("(")
            elif p == "}" and stack and stack[-1] == "{" :
                stack.pop()
            elif p == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif p == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                if p == "}" or p == "]" or p == ")":
                    return False
        if stack == []:
            return True
        else:
            return False
