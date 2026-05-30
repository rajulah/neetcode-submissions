class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyTable = {}
        for num in nums:
            frequencyTable[num] = frequencyTable.get(num, 0) + 1
        import heapq
        resultHeap = []
        heapq.heapify(resultHeap)
        for item, value in frequencyTable.items():
            heapq.heappush(resultHeap, (value,item))
            if len(resultHeap) > k:
                heapq.heappop(resultHeap)
        
        result  = []
        for i in range(k):
            result.append(heapq.heappop(resultHeap)[1])
        return result