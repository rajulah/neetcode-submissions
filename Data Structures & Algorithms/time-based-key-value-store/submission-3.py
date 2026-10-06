class TimeMap:

    def __init__(self):
        self.feelings = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.feelings:
            self.feelings[key] = []
        self.feelings[key].append((timestamp, value))
        # if key in self.feelings:
        #     feels = self.feelings[key]
        #     for i in range(len(feels)):
        #         if timestamp < feels[i][0]:
        #             feels.insert(i-1, (timestamp, value))
        #             break
        #     else:
        #         feels.append((timestamp, value))
        # else:
        #     self.feelings[key]= [(timestamp, value)]
    
    def binarySearch(self, nums: List[tuple], targetTime) -> str:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid][0] == targetTime:
                return nums[mid][1]
            elif nums[mid][0] < targetTime:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return nums[right][1]
        return ""

    def get(self, key: str, timestamp: int) -> str:
        if key in self.feelings:
            nums = self.feelings[key]
            return self.binarySearch(nums, timestamp)
        else:
            return ""
