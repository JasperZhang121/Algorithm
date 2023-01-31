class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k: return 0
        count = Counter(s)        
        if min(count.values()) >= k: return len(s)
        
        for i,c in enumerate(s):
            # If the current character appears less than k times in the string
            # We need to find the longest substring before and after it. 
            # As it cannot be included in any valid substring
            if count[c] < k:
                length1 = self.longestSubstring(s[:i], k)
                length2 = self.longestSubstring(s[i+1:], k)
                
                return max(length1, length2)
        
        return len(s)        