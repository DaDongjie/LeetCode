#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
class Solution:
    def romanToInt(self, s: str) -> int:
        
        len_s = len(s)
        if s[0] =='M': ans = 1000
        elif s[0] =='D': ans = 500
        elif s[0] =='C': ans = 100
        elif s[0] =='L': ans = 50
        elif s[0] =='X': ans = 10
        elif s[0] =='V': ans = 5
        elif s[0] =='I': ans = 1

        for i in range(1,len_s):
            if s[i] == 'M' and s[i-1] == 'C':
                ans += 800
                break
            elif s[i] == 'M':
                ans += 1000
                break
            elif s[i] == 'D' and s[i-1] == 'C':
                ans += 300
                break
            elif s[i] == 'D':
                ans += 500
                break
            elif s[i] == 'C' and s[i-1] == 'X':
                ans += 80
                break
            elif s[i] == 'C':
                ans += 100
                break
            elif s[i] == 'L' and s[i-1] == 'X':
                ans += 30
                break
            elif s[i] == 'L':
                ans += 50
                break
            elif s[i] == 'X' and s[i-1] == 'I':
                ans += 8
                break
            elif s[i] == 'X':
                ans += 10
                break
            elif s[i] == 'V' and s[i-1] == 'I':
                ans += 3
                break
            elif s[i] == 'V':
                ans += 5
                break
            elif s[i] == 'I':
                ans += 1
                
                
        return ans

def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num


