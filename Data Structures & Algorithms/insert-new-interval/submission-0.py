class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # GIVEN: non overlapping intervals
        # sorted in i[0] ascending order
        # newInterval - [start, end]
        # insert this new into existing list of intervals
        n = len(intervals)
        i = 0
        result = []

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1
        return result

        


            