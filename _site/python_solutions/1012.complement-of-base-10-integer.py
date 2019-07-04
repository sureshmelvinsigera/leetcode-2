#
# @lc app=leetcode id=1012 lang=python3
#
# [1012] Complement of Base 10 Integer
#
# https://leetcode.com/problems/complement-of-base-10-integer/description/
#
# algorithms
# Easy (57.57%)
# Total Accepted:    4.9K
# Total Submissions: 8.6K
# Testcase Example:  '5'
#
# Every non-negative integer N has a binary representation.  For example, 5 can
# be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note
# that except for N = 0, there are no leading zeroes in any binary
# representation.
# 
# The complement of a binary representation is the number in binary you get
# when changing every 1 to a 0 and 0 to a 1.  For example, the complement of
# "101" in binary is "010" in binary.
# 
# For a given number N in base-10, return the complement of it's binary
# representation as a base-10 integer.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is
# 2 in base-10.
# 
# 
# 
# Example 2:
# 
# 
# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is
# 0 in base-10.
# 
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which
# is 5 in base-10.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= N < 10^9
# 
# 
# 
# 
#

from functools import reduce
class Solution:
	def bitwiseComplement(self, N):
		ans = ''.join([str(1 - int(i)) for i in bin(N)[2:]])
		return int(ans, 2)


# s = Solution()
# print(s.bitwiseComplement(10))


