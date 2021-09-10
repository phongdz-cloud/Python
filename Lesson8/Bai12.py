# /*
#     Tìm "vị trí giá trị âm lớn nhất" trong mảng các số nguyên . Nếu mảng
#     không có giá trị âm thì trả về -1
# */
import myfuntions


def solution(n, lst):
    maxNegative = -999999
    for i in range(0, n):
        if maxNegative < lst[i] < 0:
            maxNegative = lst[i]
            indexMaxNegative = i
    return indexMaxNegative if maxNegative != -999999 else -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
