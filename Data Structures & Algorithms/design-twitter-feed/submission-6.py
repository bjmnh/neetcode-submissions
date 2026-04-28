class Twitter:

    def __init__(self):
        #Some way to keep track of users, who they follow, and what their tweetIDs are
        self.users = {}
        #I will use userID as the key, and an array of userIds + tweetIDs as the value
        
        #need a way to keep track of tweet recency
        self.tweetnum = 0

        #example:
        #{1234 : [[1235, 1236], [(0, 133), (1, 134)]] }
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.tweetnum, tweetId)
        self.tweetnum -= 1

        if userId in self.users:
            self.users[userId][1].append(tweet)
        else:
            self.users[userId] = [set([userId]),[tweet]]


    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        for followeeId in self.users[userId][0]:
            for post in self.users[followeeId][1]:
                heapq.heappush(posts,post)
        feed = []
        while posts and len(feed) < 10:
            feed.append(heapq.heappop(posts)[1])

  
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.users:
            self.users[followerId][0].add(followeeId)
        else:
            self.users[followerId] = [set([followerId, followeeId]),[]]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followerId != followeeId:
            if followeeId in self.users[followerId][0]:
                self.users[followerId][0].remove(followeeId)
            
