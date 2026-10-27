class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        result = []
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if prevEnd < start:
                result.append([prevStart, prevEnd])
                prevStart = start
                prevEnd = end
            else:
                prevStart = min(start, prevStart)
                prevEnd = max(end, prevEnd)
        result.append([prevStart, prevEnd])
        return result