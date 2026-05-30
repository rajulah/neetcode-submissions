class Solution:
    def topKFrequent(Self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        counts = [[] for i in range(len(nums) + 1)]
        for item, value in frequencyMap.items():
            counts[value].append(item)
        result = []
        for i in range(len(counts)-1, 0, -1):
            result.extend(counts[i])
            if len(result) == k:
                return result
        
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequencyTable = {}
#         for num in nums:
#             frequencyTable[num] = frequencyTable.get(num, 0) + 1
#         import heapq
#         resultHeap = []
#         heapq.heapify(resultHeap)
#         for item, value in frequencyTable.items():
#             heapq.heappush(resultHeap, (value,item))
#             if len(resultHeap) > k:
#                 heapq.heappop(resultHeap)
        
#         result  = []
#         for i in range(k):
#             result.append(heapq.heappop(resultHeap)[1])
#         return result