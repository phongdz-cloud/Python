# /*
#     Hãy liệt kê các giá trị trong mảng 1 chiều có số nguyên có chữ số đầu là số chẵn
# */
import math

import myfuntions


def findEvenNumber(n):
    while n > 10:
        n = math.floor(n / 10)
    return True if n % 2 == 0 else False


def solution(n, lst):
    arr = []
    for i in range(0, n):
        if findEvenNumber(lst[i]) and lst[i] != 0:
            arr.append(lst[i])
    return arr


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
