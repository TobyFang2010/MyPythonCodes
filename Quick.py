import os, time, random
# system(), sleep(), randint()

def outputq(q_list, times, notclean = 0):
    """
    适用于模式1与3的题目输出与交互，
    q_list: 题目元组，第1项为模式种类，第2项为数字或算式列表(列表各内容简称项目)
    time: 隔此段时间出现一个项目
    notclear: 是否保留项目显示，0表示不保留(默认)，1及以上表示在当前项目基础上保留前几个项目
    交互: 模式1输入一个答案,模式3输入列表长度个答案
    返回: 用户输入答案或答案列表
    """

def generateq(mode, max, digit):
    """
    适用于模式1与3的题目生成，
    mode: 模式种类    digit:数字位数
    max: 生成的计算笔数/试题数
    无交互，返回题目元组，用于outputq()函数
    """

def asksq(digit, max, mode):
    """
    适用于模式2的交互
    digit:数字位数  max:总试题量  mode:符号模式
    交互:依据digit和mode生成max个计算题，供用户计算，当场
    验证，返回:正确题数
    """

def shougananswer(*numbers):
    """
    生成答案
    *numbers:待特征项，可变参数，由系统提供试题
    返回:题目答案，列表或单个数字
    """

def check(usera, reala):
    """
    适用于模式1，模式3的答案验证
    usera:用户答案  reala:正确答案
    返回:是否正确 /正确个数
    """

def main():
    """
    主干函数，负责交互、计时等。模式种类：
    模式1：多笔加法、减法，加减混合计算题
    模式2：单笔多道计算题
    模式3：连续多道单笔计算题(统一给答案)
    """
    print("===== 口算训练程序 =====")
    # 选择模式
    while True:
        try:
            mode = int(input("请选择模式【1/2/3】：1多笔加减｜2单笔逐题｜3批量出题统一作答："))
            if mode in (1,2,3):
                break
            print("输入无效，请输入1、2、3")
        except ValueError:
            print("请输入数字")

    # 参数配置
    digit = int(input("请输入数字位数："))
    max_num = int(input("请输入题量："))
    use_timer = input("是否开启计时(y/n):").strip().lower() == 'y'

    start_time = time.time() if use_timer else None
    correct_count = 0

    if mode == 1 or mode == 3:
        q_list = generateq(mode, max_num, digit)
        user_ans = outputq(q_list, time=1, notclear=0)
        real_ans = shougananswer(*q_list)
        correct_count = check(user_ans, real_ans)

    elif mode == 2:
        correct_count = asksq(digit, max_num, mode)

    end_time = time.time() if use_timer else None

    # 结果输出
    total = max_num
    print(f"\n完成！正确：{correct_count}/{total}")
    if use_timer:
        cost = end_time - start_time
        print(f"总用时：{cost:.2f} 秒")


if __name__ == "__main__":
    main()
