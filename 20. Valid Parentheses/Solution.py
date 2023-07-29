class Solution:
    def isValid(self, s: str) -> bool:
        bad = {")":"(", "}":"{", "]":"["}
        stack = []
        for ch in s:
            if stack:
                if ch not in bad:
                    stack.append(ch)
                else:
                    if stack.pop() != bad[ch]:
                        return False
            else:
                stack.append(ch)
        return len(stack)==0