# -*- coding: utf-8 -*-

"""
判断一个int型数字是否是回文形式，不许用额外的空间。
"""

class Solution(object):
    def isPalindrome(self,x):
        if x < 0 :
            return False
        div = 1
        while x/div >= 10:
            div *= 10
        while x > 0:
            print(x)
            l = x // div
            print(l)
            r = x % 10

            if l != r:
                return False
            x %= div
            x //= 10
            div /= 100

        return True

if __name__ == "__main__":
    print (Solution().isPalindrome(123))
    print (Solution().isPalindrome(12321))
    print (Solution().isPalindrome(-121))