class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggestions = [list() for _ in range(len(searchWord))]
        products.sort()

        for i in range(1, len(searchWord)+1):
            word = searchWord[:i]
            
            for p in products:
                if p.startswith(word):
                    suggestions[i-1].append(p)
                    if len(suggestions[i-1]) == 3:
                        break
        
        return suggestions