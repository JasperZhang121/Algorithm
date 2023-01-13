class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        tree = defaultdict(list)
        for i, parent in enumerate(parent):
            tree[parent].append(i)
        ans = 1 
        
        def dfs(node):
            nonlocal ans 
            longest = second = 0
            for child in tree[node]:
                path_len = dfs(child)
                
                if s[child] != s[node]:
                    if path_len> longest:
                        second,longest = longest,path_len
                    elif path_len>second:
                        second = path_len
            ans = max(ans,longest+second+1)
            return longest+1
        
        dfs(0)
        return ans