#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (34.33%)
# Total Accepted:    35.8K
# Total Submissions: 104.2K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
#
#
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
#
# Note:
#
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
#
#
#

import heapq


class Solution:
    def findCheapestPrice(self, n, edges, src, dst, k):
        price = {}
        for a, b, pr in edges:
            if a not in price:
                price[a] = {b: pr}
            else:
                price[a].update({b: pr})

        visited = set()
        h = [(0, src, k + 1)]
        while h:
            p, cur, left = heapq.heappop(h)
            if cur == dst:
                return p
            visited.add(cur)
            if left > 0 and cur in price:
                for ns, pr in price[cur].items():
                    if ns in visited:
                        continue
                    heapq.heappush(h, (p + pr, ns, left - 1))
        return -1


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0

print(Solution().findCheapestPrice(n, edges, src, dst, k))
