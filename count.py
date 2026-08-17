import math
import random
print("""
欢迎使用简易计算器,
你可以在'>>>'后自由计算,
支持输入算式,
已导入math和random模块,
如:math.sqrt(2),
输入exit()退出.
快来体验吧!
""")
while True:
    a = input(">>>")
    print(eval(a))
