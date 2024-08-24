class Solution:
    def backtrack(self, current, left, right, n, results):
        # solution
        if left + right == n*2: 
            results.append(current)
        # make a choice
        if left < n:
            self.backtrack(current+"(", left+1, right, n, results)
        if right < n and right < left:
            self.backtrack(current+")", left, right+1, n, results)
        # no solution
        return
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.backtrack("", 0, 0, n, results)
        return results
