# /*
#   Kiểm tra mảng một chiều các số thực có đối xứng hay không
# */
import myfuntions


def solution(n, lst):
    i = 0
    j = n - 1
    while j > i:
        if lst[i] != lst[j]:
            return False
        i += 1
        j -= 1
    return True


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
