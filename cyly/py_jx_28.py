# -*- coding: utf-8 -*-
# @Time : 2020/7/6 9:47
# @Author : Mamamooo
# @Site :
# @File : py_jx_28.py
# @Software: PyCharm
"""

"""


def apply_discount(price,discount):
    update_price = price * (1 - discount)
    assert 0 <= update_price <= price, 'price should be greater or equal to 0 and less'
    return update_price

print( apply_discount(100,0.2))


print( apply_discount(100,2))
