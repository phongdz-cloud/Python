# /*
#   Cho mảng một chiều các số nguyên. Hãy viết hàm tìm giá trị đầu tiên thỏa mãn
#   tinh chất số gánh. (Ví dụ giá trị 12321)
# */
import math

import myfuntions


def checkReverseNumber(n):
    rev = 0
    x = n
    while n > 0:
        temp = n % 10
        n = math.floor(n / 10)
        rev = rev * 10 + temp
    return rev == x


def solution(n, lst):
    for i in range(0, n):
        if checkReverseNumber(lst[i]):
            return lst[i]
    return -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
