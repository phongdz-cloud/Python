# /*
#     Tìm "Số nguyên tố lớn nhất" trong mảng một chiều các số nguyên. Nếu mảng không có
#     số nguyên tố thì trả về số 0
# */
import myfuntions


def solution(n, lst):
    maxPrime = 0
    for i in range(0, n):
        if myfuntions.checkPrimeNumber(lst[i]) and lst[i] > maxPrime:
            maxPrime = lst[i]
    return maxPrime


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
