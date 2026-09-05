class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                j = j + result[j]
            if j < n and temperatures[j] > temperatures[i]:
                result[i] = j - i
        return result

        

        # result = [0] * len(temperatures)
        # stack = []
        # for i in range(len(temperatures)):
        #     while stack and temperatures[i] > stack[-1][0]:
        #         temp, index = stack.pop()
        #         result[index] = i - index
        #     stack.append((temperatures[i],i))
        # return result

        # result = [0]*len(temperatures)
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j-i
        #             break
        # return result


