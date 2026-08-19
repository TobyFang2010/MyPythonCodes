import time
import os


def print_wait(points=6, times=1):
    """
    友好形式打印等待提示，形如 "请稍等......"
    点数由 points 决定(默认为6)，间隔时间由 times 决定，默认为1
    """
    print("请稍等", end="", flush=True)
    for i in range(points):
        print(".", end="", flush=True)
        time.sleep(times)
    print()


def count_down(times=3, isclear=True):
    """
    倒计时！
    times 为倒计时时间，isclear 为是否清除倒计时数字
    times默认为3，isclear默认为True
    """
    for i in range(times, 0, -1):
        if isclear:
            # Linux清屏指令
            os.system("clear")
        print(i, flush=True)
        time.sleep(1)
    if isclear:
        os.system("clear")
