"""
NeetCode - Heap / Priority Queue
355. Design Twitter
Difficulty : Medium
Algorithm : Heap
Runtime : 37 ms (69.83%), Memory : 16.4 MB (84.38%)
"""

class Twitter:

    def __init__(self):
      self.tweet = defaultdict(list)    # userId : [cnt, tweetId]
      self.followId = defaultdict(set)  # followerId : set(followeeId)
      self.cnt = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
      self.tweet[userId].append((self.cnt, tweetId))
      self.cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
      feed = []
      for cnt, id in self.tweet[userId]:
        heapq.heappush(feed, (-cnt, id))
      
      if userId in self.followId.keys():
        for followeeId in self.followId[userId]:
          for cnt, id in self.tweet[followeeId]:
            heapq.heappush(feed, (-cnt, id))

      res = []
      for _ in range(10):
        if not feed:
          break
        cnt, id = heapq.heappop(feed)
        res.append(id)
      return res

    def follow(self, followerId: int, followeeId: int) -> None:
      self.followId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
      self.followId[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
