#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        
        left = 1
        right = x //2
        while left<right:
            mid = (left + right +1)//2
            squar = mid * mid
            if squar > x:
                right = mid - 1
            else:
                left = mid 
        return left

