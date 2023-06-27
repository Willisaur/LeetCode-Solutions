class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        count = 0
        while len(s) > 0:
            if len(s) > 1 and s[:2] in values:
                count += values[s[:2]]
                s = s[2:]
            else:
                count += values[s[0]]
                s = s[1:]
        return count

        