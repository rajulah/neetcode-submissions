import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = (-1) * heapq.heappop(stones)
            stone2 = (-1) * heapq.heappop(stones)
            rem = abs(stone1 - stone2)
            if rem > 0:
                heapq.heappush(stones, -1 * rem)
        return -1 * stones[0] if len(stones) > 0 else 0