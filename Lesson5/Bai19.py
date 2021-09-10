# /*
#     Nhập vào 2 bộ ngày, tháng, năm. Tính khoảng cách (số ngày) giữa hai ngày
#     vừa nhập
# */
import myfuntions
import math


def checkValid(days, d, m, y):
    if y > 0 and 1 <= m <= 12 and 1 <= d <= 31:
        if myfuntions.checkLeapYear(y) and m == 2 and d <= 29:
            return True
        if d > days[m - 1]:
            return False
        return True
    return False


def calculator(days, d, m, y, d1, m1, y1):
    if myfuntions.checkLeapYear(y):
        days[1] += 1
    sum = days[m - 1] - d
    while y != y1 or m < m1 - 1:
        m += 1
        if m == 13:
            m = 1
            y += 1
            if myfuntions.checkLeapYear(y):
                days += 1
            else:
                days[1] = 28
        sum += days[m - 1]
    sum += d1
    return sum


def solution(days, d, m, y, d1, m1, y1):
    if checkValid(days, d, m, y) and checkValid(days, d1, m1, y1):
        if m == m1 and y == y1:
            return math.fabs(d - d1)
        else:
            if y < y1 or (m < m1 and y == y1):
                result = calculator(days, d, m, y, d1, m1, y1)
            else:
                result = calculator(days, d1, m1, y1, d, m, y)
            return result
    return -1


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input())
m = int(input())
y = int(input())
d1 = int(input())
m1 = int(input())
y1 = int(input())
print(solution(days, d, m, y, d1, m1, y1))
