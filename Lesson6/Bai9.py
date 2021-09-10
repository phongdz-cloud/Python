# /*
#     Nhập vào một mảng số nguyên. Nhập tiếp một số nguyên x. Tính tổng các phần tử lớn hơn x
# */
import myfuntions


def solution(n, x, lst):
    sum = 0
    for i in range(0, n):
        if lst[i] > x:
            sum += lst[i]
    return sum


n = int(input())
x = int(input())
lst = myfuntions.myInput(n)
print(solution(n, x, lst))
