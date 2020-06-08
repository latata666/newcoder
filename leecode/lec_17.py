# -*- coding: utf-8 -*-

"""
手机按键上每个数字都对应了多个字母， 如2对应了"abc"， 现给出一个数字串， 要
求把其中的每个数字都转化为对应的字母中的一个， 列出所有的组合情况。
"""

class Solution(object):
    digit2letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def letterCombinations(self,digits):
        if not digits:
            return []
        result = []
        print ("in")
        self.dfs(digits,"",result)
        return result


    def dfs(self,digits,current,result):
        if not digits:
            print ("current",current,"result",result)
            result.append(current)
            return
        for c in self.digit2letters[digits[0]]:
            print ("current2:",current,"c:",c)
            print (digits[1:])
            self.dfs(digits[1:],current + c,result)

if __name__ == "__main__":
    print (Solution().letterCombinations("27"))