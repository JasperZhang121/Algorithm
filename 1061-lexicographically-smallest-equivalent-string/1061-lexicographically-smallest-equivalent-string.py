class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)
        ans = ""

        def dfs(root):
            if root in visited:
                return root
            visited.add(root)
            min_char = root
            for child in adj[root]:
                min_char = min(min_char, dfs(child))
            
            return min_char

        for i in range(len(s1)):
            adj[s1[i]].append(s2[i])
            adj[s2[i]].append(s1[i])

        for char in baseStr:
            visited = set()
            ans += dfs(char)
        


        return ans