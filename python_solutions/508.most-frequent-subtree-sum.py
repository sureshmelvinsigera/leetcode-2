from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (56.16%)
# Total Accepted:    58.8K
# Total Submissions: 104.6K
# Testcase Example:  '[5,2,-3]'
#
#
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
#
#
# Examples 1
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -3
#
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
#
#
# Examples 2
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -5
#
# return [2], since 2 happens twice, however -5 only occur once.
#
#
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, r):
        if not r:
            return []
        self.memo = defaultdict(int)
        self.res = []
        self.vmax = 0

        def dfs(n):
            if not n:
                return 0
            v = n.val + dfs(n.left) + dfs(n.right)
            self.memo[v] += 1
            if self.memo[v] > self.vmax:
                self.vmax = self.memo[v]
                self.res = [v]
            elif self.vmax == self.memo[v]:
                self.res.append(v)

            return v

        dfs(r)
        return self.res


s = Solution()
