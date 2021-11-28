import calendar
import datetime
from enum import IntEnum


class Weeks_jp(IntEnum):
    Mo = 0
    Tu = 1
    We = 2
    Th = 3
    Fr = 4
    Sa = 5
    Su = 6


# 何週目か返す
def get_nth_week(day):
    return (day - 1) // 7 + 1


def get_nth_dow(year, month, day):
    return get_nth_week(day), calendar.weekday(year, month, day)


# 何曜日か返す
def get_day_of_the_week(weekday):
    if weekday == Weeks_jp.Mo:
        return "月曜日"
    elif weekday == Weeks_jp.Tu:
        return "火曜日"
    elif weekday == Weeks_jp.We:
        return "水曜日"
    elif weekday == Weeks_jp.Th:
        return "木曜日"
    elif weekday == Weeks_jp.Fr:
        return "金曜日"
    elif weekday == Weeks_jp.Sa:
        return "土曜日"
    elif weekday == Weeks_jp.Su:
        return "日曜日"


def get_week(day):
    week_num = get_nth_week(day)
    return "第{}週".format(week_num)


def trush_day(day_of_the_week, week):
    print(day_of_the_week)
    print(week)
    if day_of_the_week == Weeks_jp.Mo or day_of_the_week == Weeks_jp.Th:
        return "本日は燃えるごみの収集日です"
    elif day_of_the_week == Weeks_jp.We and week == 2:
        return "本日はペットボトル収集の日です"
    elif day_of_the_week == Weeks_jp.Fr and week == 4:
        return "本日は燃えないゴミの収集日です"
    else:
        return "本日はゴミの収集日ではありません"


n = datetime.date.today()


# テストデータの作成
str_day = "2021-11-26"
test_date = datetime.datetime.strptime(str_day, "%Y-%m-%d").date()

# カレンダー表示
print(calendar.month(test_date.year, test_date.month))
print(get_day_of_the_week(test_date.weekday()))
print(get_week(test_date.day))

print(trush_day(test_date.weekday(), get_nth_week(test_date.day)))



"""

if get_nth_week(n.day) == 4 and calendar.weekday(n.year, n.month, n.day) == 5:
    print("本日は第１週月曜日です。")
elif n.weekday() == 1 and weeks == 1:
    print("本日は第1週火曜日です。")
elif n.weekday() == 2 and weeks == 1:
    print("本日は第1週水曜日です。")
elif n.weekday() == 3 and weeks == 1:
    print("本日は第1週木曜日です。")
elif n.weekday() == 4 and weeks == 1:
    print("本日は第1週金曜日です。")
elif calendar.weekday() == 5 and get_nth_week() == 4:
    print("本日は第1週土曜日です。 ")
elif n.weekday() == 6 and weeks == 1:
    print("本日は第1週日曜日です。")
    
"""
