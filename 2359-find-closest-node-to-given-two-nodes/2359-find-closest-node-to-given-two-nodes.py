class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        m1 = [-1] * len(edges)
        m2 = [-1] * len(edges)
        def dfs(node, dist, memo):
            while node != -1 and memo[node] == -1: 
                memo[node] = dist
                dist += 1
                node = edges[node] 
        
        dfs(node1, 0, m1)
        dfs(node2, 0, m2)
        minDist = float('inf')
        res = -1 
        for i in range(len(edges)):
            if m1[i] != -1 and m2[i] != -1:
                if max(m1[i], m2[i]) < minDist:
                    minDist = max(m1[i], m2[i])
                    res = i
        return res
            