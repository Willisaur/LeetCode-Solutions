class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return s == ''

        if len(p) > 1 and p[1] == '*':
            # found 0 times
            if self.isMatch(s, p[2:]):
                return True
            # found 1 or more times
            if len(s):
                i = 0
                while i < len(s) and p[0] in [s[i], '.']:
                    if self.isMatch(s[i+1:], p[2:]):
                        return True
                    i += 1
        elif len(s) and p[0] in [s[0], '.']:
            if self.isMatch(s[1:], p[1:]):
                return True
        
        return False