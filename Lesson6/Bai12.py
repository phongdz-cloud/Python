# /*
#     Nhập vào một mảng số nguyên. Nhập tiếp một số nguyên x.
#     Cho biết vị trí đầu tiên mà x có trong mảng vừa nhập. Nếu không có xuất -1
# */
import myfuntions


def solution(n, x, lst):
    for i in range(0, n):
        if lst[i] == x:
            return i
    return -1


n = int(input())
x = int(input())
lst = myfuntions.myInput(n)
print(solution(n, x, lst))
