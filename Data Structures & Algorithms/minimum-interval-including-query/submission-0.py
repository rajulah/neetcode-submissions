import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        intervals.sort()
        i = 0
        result = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                left = intervals[i][0]
                right = intervals[i][1]
                size = right - left + 1
                heapq.heappush(minHeap, (size, right))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            result[q] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]


        