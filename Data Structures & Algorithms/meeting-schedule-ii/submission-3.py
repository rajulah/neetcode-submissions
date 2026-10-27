"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key = lambda x: x.start)
        heap = [intervals[0].end]
        count = 1
        # print([(interval.start, interval.end) for interval in intervals])
        for interval in intervals[1:]:
            # print(interval.start, heap[0], len(heap), count)
            if len(heap) > 0 and heap[0] <= interval.start:
                heapq.heappop(heap)
            else:
                # print(interval.start, heap[0], len(heap), count)
                count += 1
            heapq.heappush(heap, interval.end)
        return count
                    