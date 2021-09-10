# /*
#     Nhập vào một mảng số nguyên. Nhập tiếp một số nguyên x.
#     Cho biết mảng vừa nhập có bao nhiêu phần tử bằng x
# */
import myfuntions


def solution(n, x, lst):
    count = 0
    for i in range(0, n):
        if lst[i] == x:
            count += 1
    return count


n = int(input())
x = int(input())
lst = myfuntions.myInput(n)
print(solution(n, x, lst))
