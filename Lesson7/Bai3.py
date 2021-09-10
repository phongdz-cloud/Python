# /*
#    Tìm "nguyên tố cuối cùng" trong mảng một chiều các số nguyên. Nếu mảng không có
#    số nguyên tố thì trả về -1;
# */
import myfuntions


def solution(n, lst):
    findLastPrimeNumber = -1
    for i in range(0, n):
        if myfuntions.checkPrimeNumber(lst[i]):
            findLastPrimeNumber = lst[i]
    return findLastPrimeNumber


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
