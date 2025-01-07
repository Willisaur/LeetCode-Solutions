class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrs = words.copy()
        out = []
        for s in substrs:
            for w in words:
                if s in w and s != w:
                    out.append(s)
                    break
        return out