class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # break s into words as a list
        # if len(pattern) != len(words), it is not onto, so return False
        # iterate using pattern as a guide
        # use a dict to with pattern letters and words
        # if keys conflict, return False
        # if at any point the current pattern does not equal the given pattern, return False
        # return True at the end

        words = s.split(" ")

        if len(pattern) != len(words):
            return False
        
        mapper = dict()

        for i in range(len(pattern)):
            if mapper.get(pattern[i], -1) == -1:
                if words[i] in mapper.values():
                    return False
                else:
                    mapper[pattern[i]] = words[i]
            elif mapper[pattern[i]] != words[i]:
                return False
            
        return True
        
        # i originally failed to account for the fact that len(pattern) doesn't necessarily equal the number of words in s, creating overflow errors or false positives
        # also,  I was unsure if pattern had to start with "a" and continue alphabetically
        