class Solution:
    def isValid(self, s: str) -> bool:
        compliments = {'}':'{', ')':'(', ']':'['}
        open = {'{', '(', '['}
        stack = []
        for ch in s:
            if ch in open:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] == compliments[ch]:
                    stack.pop(-1)
                else:
                    return False

        return not stack
