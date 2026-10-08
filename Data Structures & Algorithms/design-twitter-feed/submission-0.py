import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetmap[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []
        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if len(self.tweetmap[followee]) < 1:
                continue
            index = len(self.tweetmap[followee]) - 1
            time, tweetId = self.tweetmap[followee][index]
            heapq.heappush(heap,(time, tweetId, followee, index))
        
        while heap and len(result) < 10:
            time, tweetId, followeeId, oldIndex = heapq.heappop(heap)
            newIndex = oldIndex - 1
            result.append(tweetId)
            if newIndex >= 0:
                time, tweetId = self.tweetmap[followeeId][newIndex]
                heapq.heappush(heap, (time, tweetId, followeeId, newIndex))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
