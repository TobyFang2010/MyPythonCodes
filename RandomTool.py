# coding=utf-8
#!/usr/bin/env python3
import random
import time

def choosing_option(optlist, is_realrandom):
    """
    随机选择核心函数
    :param optlist: 传入的选项列表
    :param is_realrandom: 布尔值，True=高消耗自然随机，False=低消耗伪随机
    :return: 最终选中的单个选项字符串
    """
    # 拷贝原列表，shuffle为原地操作，避免修改外部原始选项库
    opt = optlist.copy()
    random.shuffle(opt)

    if not is_realrandom:
        # 伪随机模式：仅打乱一次列表，直接取第一个元素，运算开销极小
        return opt[0]
    else:
        # 自然随机模式：模拟多次随机运算消耗
        result = ""
        # 随机生成5~20次循环次数，模拟不定量重复抽取
        loop_times = random.randint(5, 20)
        for _ in range(loop_times):
            # 在合法下标范围内随机取索引
            idx = random.randint(0, len(opt) - 1)
            # 循环不断覆盖结果，仅保留最后一次抽取的值作为最终结果
            result = opt[idx]
        return result

def main():
    # 程序欢迎引导文本
    welcome_text = (
        "您好,这里是随机选择器(均等可能性).请输入你指定的选项,将其加入选项库中;"
        "若想加入相同的选项,请用前后缀加以区分;若输入内容已在选项库中存在,则删除该选项."
        "您可以随时使用指令“/list”展示当前的选项库;“/quit”完成选择并退出输入模式."
    )
    print(welcome_text)
    # 存储所有用户输入的选项
    user_opt = []

    # 持续接收用户输入的主循环
    while True:
        # strip()去除输入首尾空格，规避多余空格导致匹配失败
        current_opt = input(">>> ").strip()

        # 退出输入循环指令
        if current_opt == "/quit":
            break
        # 查看全部现有选项指令
        elif current_opt == "/list":
            print("当前选项库：")
            for item in user_opt:
                print(f" - {item}")
        # 输入内容已存在列表中，执行删除并给出反馈
        elif current_opt in user_opt:
            user_opt.remove(current_opt)
            print(f"已删除选项：{current_opt}")
        # 全新选项，直接加入列表，无控制台反馈
        else:
            user_opt.append(current_opt)

    # 输入阶段结束，打印全部待随机选项供用户核对
    print("\n===== 待随机的全部选项 =====")
    for item in user_opt:
        print(item)
    print("============================\n")
    print("请再次确认以上选项是否正确！是否执行随机？")
    ask = input("y/n，默认为y \n>>> ").strip()
    # 用户选择取消，直接结束程序
    if ask == "n":
        print("您已取消本次随机操作")
        return 0

    # 判断是否启用高消耗随机模式
    print("设备能否承受多次运算带来的消耗？")
    ask = input("y/n，默认为y \n>>> ").strip()
    # 一行布尔简化赋值，输入n则关闭自然随机，其余情况默认开启
    flag = False if ask == "n" else True

    # 加载等待动画，flush=True强制实时打印，消除缓冲区延迟
    print("请稍候", end="", flush=True)
    for _ in range(6):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)

    # 调用核心随机函数，输出最终结果
    res = choosing_option(user_opt, flag)
    print(f"\n最终随机结果为：{res}")
    return 0

# 程序入口，仅直接运行文件时执行主函数
if __name__ == "__main__":
    main()