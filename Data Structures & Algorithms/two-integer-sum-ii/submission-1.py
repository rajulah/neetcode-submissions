class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sumOf = numbers[left] + numbers[right]
            if sumOf == target:
                return [left+1, right+1]
            elif sumOf < target:
                left = left+1
            else:
                right = right-1
        return [-1,-1]
        
        
        # seen = {}
        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     if complement in seen:
        #         return [seen[complement]+1,i+1]
        #     seen[numbers[i]] = i
        # return [0,0]