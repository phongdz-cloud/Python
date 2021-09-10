# /*
#     Nhập vào một mảng số nguyên. Nhập tiếp một số nguyên x.
#     Cho biết x có trong mảng vừa nhập hay không? Nếu có xuất 1, nếu không xuất số 0
# */
import myfuntions


def solution(n, x, lst):
    for i in range(0, n):
        if lst[i] == x:
            return 1
    return 0


n = int(input())
x = int(input())
lst = myfuntions.myInput(n)
print(solution(n, x, lst))
