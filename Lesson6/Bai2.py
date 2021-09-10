# /*
#     Nhập vào mảng các số thực. Tính tổng các phần tử trong mảng
# */
import myfuntions


def solution(n, lst):
    sum = 0
    for i in range(0, n):
        sum += lst[i]
    return sum


n = int(input())
lst = myfuntions.myInputFloat(n)
print(solution(n, lst))
