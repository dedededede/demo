# -*- encoding: utf8 -*-
from sympy import poly
from sympy.abc import x
f1 = 1 + x  # 1个1克的砝码
f2 = 1 + x**2  # 1个2克的砝码
f3 = 1 + x**3  # 1个3克的砝码
f4 = 1 + x**4  # 1个4克的砝码

print poly(f1 * f2 * f3 * f4)
