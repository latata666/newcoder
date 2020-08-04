# -*- coding: utf-8 -*-
# @Time : 2020/7/6 10:59
# @Author : Mamamooo
# @Site :
# @File : py_jx_30.py
# @Software: PyCharm
"""

"""

import unittest

def sort(arr):
    l = len(arr)
    for i in range(0,1):
        for j in range(i+1,l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp



class TestSort(unittest.TestCase):
    def test_sort(self):
        arr = [3,4,1,5,6]
        sort(arr)
        self.assertEqual(arr,[1,3,4,5,6])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'],exit=False)

