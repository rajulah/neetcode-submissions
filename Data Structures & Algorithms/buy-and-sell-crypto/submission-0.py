class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightArray = [0] * len(prices)
        leftArray = [0] * len(prices)
        leftArray[0] = prices[0]
        rightArray[-1] = prices[-1]
        for i in range(1, len(prices)):
            leftArray[i] = min(leftArray[i-1], prices[i])
        for i in range(len(prices)-2, -1, -1):
            rightArray[i] = max(rightArray[i+1], prices[i])
        print(leftArray, rightArray)
        for i in range(len(prices)):
            prices[i] = rightArray[i] - leftArray[i]
        return max(prices)
