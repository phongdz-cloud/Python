# /*
#    Tìm "số nguyên tố đầu tiên" trong mảng một chiều các số nguyên. Nếu mảng không có
#    số nguyên tố thì trả về -1;
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n):
        if myfuntions.checkPrimeNumber(lst[i]):
            return lst[i]
    return -1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
