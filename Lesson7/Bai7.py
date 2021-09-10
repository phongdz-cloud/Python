# /*
#    Viết chương trình tính tổng số chính phương trong mảng n phần tử
# */
import myfuntions


def solution(n, lst):
    sum = 0
    for i in range(0, n):
        if myfuntions.checkSquareNumber(lst[i]):
            sum += lst[i]
    return sum


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
