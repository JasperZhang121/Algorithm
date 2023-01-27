class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        g, res, n= defaultdict(list), [] , len(graph)
        for i, v in enumerate(graph):
            for x in v:
                g[i].append(x)
        
        
        def dfs(node, temp, res):
            if temp!=[] and temp[-1]==n-1:
                res.append(temp[:])
                return
            
            children = g[node]

            for x in children:
                temp.append(x)
                dfs(x,temp,res)
                temp.pop()
        
        dfs(0,[0],res)
        return res