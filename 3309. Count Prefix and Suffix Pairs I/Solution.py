class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefixes = set()
        suffixes = set()

        count = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                count += words[j].startswith(words[i]) and words[j].endswith(words[i])

        return count