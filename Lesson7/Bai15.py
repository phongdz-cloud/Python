# /*
#   Viết chương trình kiểm tra các phần tử trong một mảng có lập thành cấp
#   số cộng hay không.
# */
import myfuntions


def checkValid(n):
    return True if n >= 2 else False


def solution(n, lst):
    if checkValid(n):
        k = lst[1] - lst[0]
        for i in range(0, n - 1):
            if lst[i + 1] - lst[i] != k:
                return False
        return True
    return False


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
