class Solution:
    def timeToEat(self, piles, k):
        total = 0
        for p in piles:
            total += math.ceil(float(p) / k)
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            time = self.timeToEat(piles, mid)
            if time <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
            
