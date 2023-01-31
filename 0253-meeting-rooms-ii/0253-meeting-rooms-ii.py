class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        start = [intervals[i][0] for i in range(n)]
        end = [intervals[i][1] for i in range(n)]
        
        start.sort(); end.sort()
        
        i,j,count,res = 0,0,0,0
        
        while i<n and j<n:
            if start[i]<end[j]:
                count+=1
                i+=1
                res = max(count,res)
            else:
                count-=1
                j+=1
                
        
        return res