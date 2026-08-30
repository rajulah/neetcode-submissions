class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        result = 0
        while left < right:
            if leftMax > rightMax:
                right -= 1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]

            else:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]
            # result += abs(height[left] - leftMax)
            # result += abs(height[right] - rightMax)
            # leftMax = max(height[left], leftMax)
            # rightMax = max(height[right], rightMax)
            # left += 1
            # right -= 1
            # print(leftMax, left, rightMax, right, result)
        return result