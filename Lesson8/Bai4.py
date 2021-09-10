# /*
# Tìm giá trị đầu tiên trong mảng 1 chiều các số nguyên có chữ số đầu tiên là chữ số lẻ (dauledautien)
# Nếu trong mảng không tồn tại giá trị như vậy hàm trả về giá trị 0
# */
import math

import myfuntions


def checkOddNumber(n):
    while n > 10:
        n = math.floor(n / 10)
    return n % 2 != 0


def solution(n, lst):
    for i in range(0, n):
        if checkOddNumber(lst[i]):
            return lst[i]
    return 0


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
