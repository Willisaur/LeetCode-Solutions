class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        output = [0] * len(queries)
        arr = [0] * len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(words)):
            arr[i] = (words[i][0] in vowels and words[i][-1] in vowels) + arr[i-1]

        for i in range(len(queries)):
            l, r = queries[i]
            if l == 0:
                output[i] = arr[r]
            else:
                output[i] = arr[r] - arr[l-1]

        return output