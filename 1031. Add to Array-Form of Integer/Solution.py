class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        newNum = 0
        for i in range(len(num) - 1, -1, -1):
            newNum += num[i] * 10 ** (len(num) - i - 1)
        newNum += k

        arrayForm = []
        i = 0
        while newNum > 0:
            arrayForm.insert(0, newNum % 10)
            i += 1
            newNum //= 10
        
        return arrayForm