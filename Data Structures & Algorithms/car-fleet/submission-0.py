class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position, speed)]
        cars = sorted(cars)
        stack = []
        for i in range(len(cars)-1,-1,-1):
            stack.append((target - cars[i][0])/cars[i][1])
            if len(stack) >= 2 and stack [-1] <= stack[-2]:
                stack.pop()
        return len(stack)


