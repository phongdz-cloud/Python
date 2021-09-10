# /*
#     Viết chương trình kiểm tra các phần tử trong một mảng có gồm toàn các
#     số lẻ hay không
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n):
        if lst[i] % 2 == 0:
            return False
    return True


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
