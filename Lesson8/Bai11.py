# /*
#     Tìm "giá trị chẵn nhỏ nhất" trong mảng một các số nguyên. Nếu mảng không có giá trị
#     chẵn thì trả về giá trị không chẵn là -1;
# */
import myfuntions


def solution(n, lst):
    minEvennumber = 999999
    for i in range(0, n):
        if lst[i] % 2 == 0 and lst[i] < minEvennumber:
            minEvennumber = lst[i]
    return minEvennumber if minEvennumber != 999999 else -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
