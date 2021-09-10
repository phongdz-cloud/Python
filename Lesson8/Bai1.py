# /*
#   Ta định nghĩa 1 mảng có tính chất chẵn lẻ, khi tổng của 2 phần tử liên tiếp luôn là số lẻ.
#   Viết hàm kiểm tra mảng có tính chất chẵn lẻ hay không
# */
import myfuntions


def solution(n, lst):
    if n == 1:
        return False
    for i in range(0, n - 1):
        if (lst[i] + lst[i + 1]) % 2 == 0:
            return False
    return True


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
