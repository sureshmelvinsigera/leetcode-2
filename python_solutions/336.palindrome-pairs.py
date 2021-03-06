#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (31.02%)
# Total Accepted:    70.1K
# Total Submissions: 225.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in
# the given list, so that the concatenation of the two words, i.e. words[i] +
# words[j] is a palindrome.
#
# Example 1:
#
#
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
#
# Example 2:
#
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
#
#
#
#


class Solution:
    def isp(self, str):
        return str == str[::-1]

    def palindromePairs(self, words):
        res = set()
        m = {}
        for i, w in enumerate(words):
            m[w[::-1]] = i

        for i, w in enumerate(words):
            if w == "":
                for j, u in enumerate(words):
                    if self.isp(u):
                        res.add((i, j))

            for j in range(len(w)):
                if w[0:j] in m and self.isp(w[j:]):
                    res.add((i, m[w[0:j]]))

                if w[j:] in m and self.isp(w[0:j]):
                    res.add((m[w[j:]], i))

        return [[i, j] for (i, j) in res if i != j]


s = Solution()
words = ["bat", "tab", "cat"]
words = ["abcd", "dcba", "lls", "s", "sssll", ""]
print(s.palindromePairs(words))
