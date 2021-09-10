# /*
# Viết chương trình tìm số âm lớn nhất trong một mảng các số nguyên
# */
import myfuntions


def solution(n, lst):
    maxNegative = -9999999
    for i in range(0, n):
        if maxNegative < lst[i] < 0:
            maxNegative = lst[i]
    return maxNegative


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
