class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # Union-Find template without ranking optimization.
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            UF[find(x)] = find(y)
            
            
        #get the nodes with the same value easily.    
        tree = defaultdict(list)
        val2Nodes = defaultdict(set)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        

        res = len(vals)        
        # Sort and union the nodes
        for v in sorted(val2Nodes.keys()):
            # Union elements with its neighbor if its neighbor smaller.
            for node in val2Nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node,nei)
            # each group, count the number of elements with value==v in this group.
            groupCount = defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[find(node)] += 1
                
            for root in groupCount.keys():
                res += comb(groupCount[root],2)
        
        return res
         
        
        
            
        
        
        