import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 2d array -> points
        # distance from origin = sqrt(x2 + y2)
        def distance(x1, x2):
            return math.sqrt((x1)**2 + (x2)**2)

        pointsDistance = [(distance(p[0], p[1]), p) for p in points]
        heapq.heapify(pointsDistance)
        result = []
        while k > 0:
            point = heapq.heappop(pointsDistance)
            result.append(point[1])
            k -= 1
        return result