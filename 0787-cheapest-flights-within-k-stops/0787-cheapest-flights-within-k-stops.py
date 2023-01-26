class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(dict)
        for u, v, p in flights:
            graph[u][v] = p
        
        seen = {}
        pq = []
        heappush(pq, (0, 0, src))
        
        while pq:
            cost, hops, city = heappop(pq)
            seen[city] = hops
            
            if city == dst:
                return cost
            
            if hops > k:
                continue
            
            for next_city, next_cost in graph[city].items():
                if next_city in seen and seen[next_city] <= hops:
                    continue
                heappush(pq, (cost + next_cost, hops + 1, next_city))
        
        return -1
