class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = dict()

        for ch in magazine:
            if ch in magDict:
                magDict[ch] += 1
            else:
                magDict[ch] = 1
        
        for ch in ransomNote:
            if ch not in magDict.keys() or magDict[ch] == 0:
                return False
            else:
                magDict[ch] -= 1
        
        return True

        # be careful which string you use your dict for!