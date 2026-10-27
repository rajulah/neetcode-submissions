class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertStart = newInterval[0]
        insertEnd = newInterval[1]
        i = 0
        while i < len(intervals) and insertStart > intervals[i][1]:
            i += 1
        
        if i == len(intervals):
            intervals.append(newInterval)
            return intervals
        
        while i < len(intervals) and insertEnd >= intervals[i][0]:
            insertStart = min(insertStart, intervals[i][0])
            insertEnd = max(insertEnd, intervals[i][1])
            del intervals[i]
            # print("inside ", insertStart, insertEnd)
        
        intervals.insert(i, [insertStart, insertEnd])

        return intervals