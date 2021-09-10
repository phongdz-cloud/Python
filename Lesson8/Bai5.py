# /*
# Ta định nghĩa 1 mảng được gọi là dạng sóng khi phần tử có trị số i
# lớn hơn hoặc nhỏ hơn 2 phần tử xung quanh. Hãy viết hàm kiểm tra mảng có dạng sóng không
# */
import myfuntions


def checkWave(a, b, c):
    return (a > b and a > c) or (a < b and a < c)


def solution(n, lst):
    if n < 3:
        return 0
    for i in range(1, n - 1):
        if checkWave(lst[i], lst[i - 1], lst[i + 1]):
            return lst[i]
    return 0


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
