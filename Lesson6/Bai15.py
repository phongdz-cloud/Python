# /*
#     Viết hàm tìm "số chẵn đầu tiên" trong mảng các số nguyên.
#    nếu mảng không có giá trị chẵn thì hàm sẽ trả về giá trị không chẵn là -1
# */
import myfuntions


def solution(n, lst):
    for i in range(n):
        if lst[i] % 2 == 0:
            return lst[i]
    return -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
