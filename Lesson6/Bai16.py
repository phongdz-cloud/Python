# /*
#    Tìm "số nguyên dương cuối cùng" trong mảng số nguyên có n phần tử.
#     Nếu mảng không có giá trị dương thì trả về giá trị -1
# */
import myfuntions


def solution(n, lst):
    positiveNumber = -1
    for i in range(0, n):
        if lst[i] > 0:
            positiveNumber = lst[i]
    if positiveNumber != -1:
        return positiveNumber
    return -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
