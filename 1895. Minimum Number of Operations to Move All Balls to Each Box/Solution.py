class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []

        for i in range(len(boxes)):
            amnt = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    amnt += abs(i-j)
            arr.append(amnt)
        return arr