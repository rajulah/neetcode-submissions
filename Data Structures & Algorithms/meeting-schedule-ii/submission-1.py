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

        heap = []
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)

        # n = len(intervals)
        # if n < 2:
        #     return n
        # intervals.sort(key = lambda x: x.end)
        # rooms = 1
        # 5-10, 15-20, 0-40
        # prevEnd = intervals[0].end
        # for interval in intervals[1:]:
        #     if interval.start >= prevEnd:
        #         prevEnd = interval.end
        #         continue
        #     else:
        #         rooms += 1
        #         prevEnd = max(interval.end, prevEnd)
        # return rooms
        