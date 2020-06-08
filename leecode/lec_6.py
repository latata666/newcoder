# -*- coding: utf-8 -*-

"""
将所给字符串按特定形状排列，依次将每排的字符连接形成新的字符串
"""


class Solution(object):
    def convert(self,s,numRows):
        if numRows < 1:
            return s
        result = ''
        index  = 0
        n = len(s)
        for i in range(0,numRows):
            if i == 0 or i == numRows - 1 :
                while index < n:
                    result += s[index]
                    index += 2 * numRows -2
                index = i + 1
            else:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2 * i - 2
                    if index >= n:
                        break
                    result += s[index]
                    index += 2 * i
                index = i + 1
        print(result)
        return result

# Test cases
if __name__ == "__main__":
    Solution().convert("PAYPALISHIRING", 2)
    Solution().convert("PAYPALISHIRING", 3)
    Solution().convert("PAYPALISHIRING", 4)