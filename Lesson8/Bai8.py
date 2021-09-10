# /*
# Tìm số "âm lớn nhất" trong mảng một chiều các số thực.
#  Nếu mảng không có giá trị âm thì trả về giá trị 0.
# */
import myfuntions


def solution(n, lst):
    maxNegative = -999999
    for i in range(0, n):
        if maxNegative < lst[i] < 0:
            maxNegative = lst[i]
    return maxNegative


n = int(input())
lst = myfuntions.myInputFloat(n)
print(solution(n, lst))
