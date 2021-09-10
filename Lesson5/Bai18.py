# /*
#     Nhập vào ngày ,tháng,năm. Hỏi từ ngày vừa nhập đến ngày đầu tiên của năm tiếp theo là bao nhiêu ngày
# */
import myfuntions


def checkValid(days, d, m, y):
    if y > 0 and 1 <= m <= 12 and 1 <= d <= 31:
        if myfuntions.checkLeapYear(y):
            days[1] += 1
        if d > days[m - 1]:
            return False
        return True
    return False


def solution(days, d, m, flag):
    if flag:
        sum = days[m - 1] - d
        while 1:
            m += 1
            if m > 12:
                break
            sum += days[m - 1]
        return sum + 1
    return -1


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input())
m = int(input())
y = int(input())
flag = checkValid(days, d, m, y)
result = solution(days, d, m, flag)
print(result if flag else "Ngày tháng năm không hợp lệ")
