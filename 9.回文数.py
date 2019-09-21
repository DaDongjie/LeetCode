#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = 0
        if x < 0:
            flag = 1
        else:
            str_x = str(x)
            len_x = len(str_x)
            for i in range(len_x//2):
                if str_x[i] != str_x[len_x-i-1]:
                    flag=1
                    break
        if flag == 1:
            return False
        else:
            return True
                   

