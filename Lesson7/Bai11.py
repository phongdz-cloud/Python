# /*
#     Viết chương trình kiểm tra các phần tử có tăng liên tục hay không
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
