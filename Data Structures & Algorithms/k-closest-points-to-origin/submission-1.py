import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            heapq.heappush(heap, (-1 * dist, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(heap) > 0:
            i = heapq.heappop(heap)[1]
            result.append(points[i])
        return result
