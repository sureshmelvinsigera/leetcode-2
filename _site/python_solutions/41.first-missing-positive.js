/*
 * @lc app=leetcode id=41 lang=javascript
 *
 * [41] First Missing Positive
 *
 * https://leetcode.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (28.67%)
 * Total Accepted:    206.5K
 * Total Submissions: 719.7K
 * Testcase Example:  '[1,2,0]'
 *
 * Given an unsorted integer array, find the smallest missing positive
 * integer.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,0]
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,4,-1,1]
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [7,8,9,11,12]
 * Output: 1
 * 
 * 
 * Note:
 * 
 * Your algorithm should run in O(n) time and uses constant extra space.
 * 
 */
/**
 * @param {nums[]} nums
 * @return {numbs}
 */
var firstMissingPositive = function(nums) {
    for (var i = 0; i < nums.length; i++) {
        var n = nums[i];
        if (n <= 0 || n > nums.length || n == i + 1) continue;
        while (true) {
            var tmp = nums[n - 1];
            nums[n - 1] = n;
            if (tmp <= 0 || tmp > nums.length || tmp == n) break;
            n = tmp;
        }
    }

    for (var i = 0; i < nums.length; i++)
        if (i + 1 != nums[i])
            return i + 1;
    return 1 + nums.length;
};