class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        x, y = set(), set()
        
        for _ in range(len(edges)):
            print(node1, node2)
            if node1 in y and node2 in x:
                return min(node1, node2)
            if node1 in y:
                return node1
            if node2 in x:
                return node2
            if node1 == node2:
                return node1
            
            if node1 != -1:
                x.add(node1)
                node1 = edges[node1]
            if node2 != -1:
                y.add(node2)
                node2 = edges[node2]
        
        return -1