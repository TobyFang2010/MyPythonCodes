import math
import random
print("""
欢迎使用简易计算器
你可以在">>>"后自由计算
支持输入算式
支持用math和random模块
如:math.sqrt(2)
输入完算是按下回车
cmd格式输出答案
快来体验吧
""")
while True:
    a = input(">>>")
    print(eval(a))