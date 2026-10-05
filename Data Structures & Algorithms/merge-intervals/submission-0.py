class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x[0])
        result = []
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if currEnd < intervals[i][0]:
                result.append([currStart, currEnd])
                currStart, currEnd = intervals[i]
                continue
            elif currEnd >= intervals[i][0]:
                currEnd = max(currEnd, intervals[i][1])
                currStart = min(currStart, intervals[i][0])
        result.append([currStart, currEnd])
        return result