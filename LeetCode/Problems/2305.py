# Daily challenge in 2023.07.01
# 2305. Fair Distribution of Cookies
# difficulty : Medium
# algorithm : Recursion(top-down)
# Runtime : 75 ms (73.13%), Memory : 19.2 MB (5.60%)
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def rec(self, dist = [0]*k, index = 0):
            nonlocal cookies_size, k, unfair, check_list
            tuple_dist = tuple(dist)
            if tuple_dist in check_list:
                return
            else:
                check_list.add(tuple_dist)

            if index == cookies_size:
                unfair = min(unfair, max(dist))
                return

            for i in range(k):
                next_dist = dist[::]
                next_dist[i] += cookies[index]
                next_dist.sort()
                rec(self, next_dist, index+1)

        check_list = set([])
        cookies_size, unfair = len(cookies), 10**9
        rec(self)
        return unfair
