import datetime
import sys

def parse_date_argument():
    """解析命令行日期参数，返回日期对象"""
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("错误：无效的日期格式，必须使用YYYY‑MM‑DD格式")
            sys.exit(1)
    return datetime.date.today()


def get_exam_day_info(date):
    """返回指定日期的考试科目信息"""
    day = date.day
    return {
        14: "语文（上午）、物理/化学（下午）",
        15: "数学（上午）、道德与法治/历史（下午）",
        16: "英语（上午）",
        17: "生物地理（下午）"
    }.get(day)


current_date = parse_date_argument()

# 处理看考场时间（6月13日下午）
if current_date.month == 6 and current_date.day == 13:
    print("看考场（下午）")
    next_exam = datetime.date(current_date.year, 6, 14)
    delta = next_exam - current_date
    print(f"距离{current_date.year}年中考还有：{delta.days}天")

elif 14 <= current_date.day <= 17 and current_date.month == 6:
    exam_info = get_exam_day_info(current_date)
    print(f"今天是中考第{current_date.day - 13}天：")
    print(exam_info)

else:
    # 计算下一次中考日期
    if current_date.month < 6 or (current_date.month == 6 and current_date.day < 14):
        next_year = current_date.year
    else:
        next_year = current_date.year + 1

    next_exam = datetime.date(next_year, 6, 14)
    delta = next_exam - current_date
    print(f"距离{next_year}年中考还有：{delta.days}天")
