class Twitter:

    def __init__(self):
        self.count = 0
        self.follower_map = defaultdict(set)  # userId -> set of foloweeId
        self.tweet_map = defaultdict(list)  # userId -> list of [count, tweetIds]
        #(userID, [(time, tweetId), (time+1, tweetId)])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        # ensure that user follows themself
        self.follower_map[userId].add(userId)
        
        # smaller time means that the tweet is more recent
        for followerId in self.follower_map[userId]:
            if followerId in self.tweet_map:
                index = len(self.tweet_map[followerId]) - 1
                count, tweetId = self.tweet_map[followerId][index]
                heapq.heappush(min_heap, [count, tweetId, followerId, index - 1])
                
        while min_heap and len(res) < 10:
            count, tweetId, followerId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            # add next tweet from the same user
            if index >= 0:
                count, tweetId = self.tweet_map[followerId][index]
                heapq.heappush(min_heap, [count, tweetId, followerId, index - 1])

        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
            