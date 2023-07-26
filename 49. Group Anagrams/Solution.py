class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each str alphabetically
        # use a dict to store the anagram index in the output array's
        # pass through strs a second time to know which words are anagrams to return

        output = [] # list of lists
        mapper = dict() # sorted str: index
        x = 0

        for i in range(len(strs)):
            s_str = "".join(sorted(strs[i]))
            if s_str not in mapper:
                mapper[s_str] = x
                x += 1

        for i in range(len(strs)):
            s_str = "".join(sorted(strs[i]))
            if len(output) - 1 < mapper[s_str]:
                output.append(list())
            output[mapper[s_str]].append(strs[i])
        
        return output