def starter():
    """
    显示开头以及倒计时，无参数及返回值
    """
    import PrintForWait
    print("\033c", end="")        # Linux命令,暂不适配Win
    input("等待按回车开始(Enter确认)")
    print("\033c", end="")
    PrintForWait.count_down()


def outputq(q_list, times, notclear=False):
    """
    省略文档,仅提示被修改的参数:
    notclear: 是否保留项目显示 False不保留(默认),True全部保留
    """
    import time
    starter()
    for i in q_list[1]:
        print(i, flush=True)
        time.sleep(times)

    if not notclear:
        print("\033c", end="")

    if q_list[0] == 1:
        while True:
            try:
                user = int(input("请作答\n>>>"))
            except ValueError:
                print("接收到非数字字符。若无法计算,请输入0")
            else:
                return user

    elif q_list[0] == 3:
        # 暂不实现,具体抽取作答过程,可参见上.
        pass
    else:
        raise ValueError("The function only support mode 1 or 3.")


def checkanswer(usera, q_list):
    """
    本函数由showganswer()和check()合并而来,用于题目(模式1与3)的答案验证
    usera:用户答案 q_list:题目元组
    """
    if q_list[0] == 1:
        sum = 0
        for i in q_list[1]:
            sum += i
        print("正确答案是:", sum)
        if usera == sum:
            print("正确!")
        else:
            print("错误!")
    elif q_list[0] == 3:
        pass    # 暂时不实现
    else:
        raise ValueError("The function only support mode 1 or 3.")


def generateq(mode, max, digit):
    import random
    if int(digit) < 1:
        raise ValueError("The digit must not smaller than 1.")
    else:
        max_num = 10 ** (int(digit)+1) - 1
        min_num = 10 ** (int(digit)-1)
        q_list = []
        for i in range(max):
            if mode[0] == 1:
                if mode[1] == True and (random.randint(1,10) % 2 == 0):
                    q_list.append(random.randint(-max_num, -min_num))
                else:
                    q_list.append(random.randint(min_num, max_num))
            elif mode[0] == 3:
                pass    # 暂不实现
            else:
                raise ValueError("The function only support mode 1 or 3.")
        return (mode[0], q_list)


def asksq(digit, max):
    """
    改为四则运算,不含除法
    """
    import random
    print("\033c", end="")
    input("INFORMATION")
    if int(digit) < 1:
        raise ValueError("The digit must not smaller than 1.")
    else:
        max_num = 10 ** (int(digit)+1) - 1
    starter()
    results = {}
    corrects = []
    for i in range(max):
        first_num = random.randint(-max_num, max_num)
        type = ""
        temp = random.randint(0, max_num) % 3
        match temp:
            case 0: type = '+'
            case 1: type = '-'
            case 2: type = '*'
        second_num = random.randint(-max_num, max_num)
        question = str(first_num) + type + (str(second_num) if second_num > 0 else ("(" + str(second_num) + ")"))

        while True:
            try:
                user = int(input(question))
            except ValueError:
                print("接收到非法字符")
            else:
                break

        match temp:
            case 0: result = first_num + second_num
            case 1: result = first_num - second_num
            case 2: result = first_num * second_num

        results[i+1] = result
        if user == result:
            corrects.append(result)

        print("本题正确答案是")
        for key,value in results.items():
            print("第{}题:{}".format(key,value))
        print("答对了!",end='')
        for i in corrects:
            print("第{}题".format(i),end=",")
        print("!")
