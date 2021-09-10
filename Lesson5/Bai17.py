# /*
#     Nhập vào ngày, tháng, năm. Hỏi từ ngày vừa nhập là ngày thứ bao nhiêu trong năm?
#     (Tính khoảng cách từ ngày đầu năm đến ngày vừa nhập)
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
        count = 0
        i = 1
        while i <= 12:
            if i == m:
                count += d
                break
            count += days[i - 1]
            i += 1
        return count
    return -1


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input())
m = int(input())
y = int(input())
flag = checkValid(days, d, m, y)
result = solution(days, d, m, y)
print(result if flag else "Ngày tháng năm không hợp lệ")
