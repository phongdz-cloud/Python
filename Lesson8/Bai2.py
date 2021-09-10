# /*
#   Kiểm tra mảng số nguyên có tồn tại 2 giá trị 0 liên tiếp hay không?
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n - 1):
        if lst[i] == 0 and lst[i + 1] == 0:
            return True
    return False


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
