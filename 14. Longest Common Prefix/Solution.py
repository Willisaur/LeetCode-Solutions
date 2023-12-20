class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children = dict()

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                currentNode = self.root
                for ch in word:
                    if ch not in currentNode.children:
                        currentNode.children[ch] = TrieNode()
                    currentNode = currentNode.children[ch] 

            def search(self, word):
                count = 0
                currentNode = self.root
                for ch in word:
                    if ch not in currentNode.children:
                        return count
                    currentNode = currentNode.children[ch]
                    count += 1
                return count
        

        trie = Trie()
        trie.insert(strs[0])
        mostInCommon = len(strs[0])

        for s in strs[1:]:
            mostInCommon = min(mostInCommon, trie.search(s))

        return strs[0][:mostInCommon]
