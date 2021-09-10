# //Liệt kê các số nguyên tố nhỏ hơn n
import myfuntions


def solution(n):
    lst = []
    for i in range(0, n):
        if myfuntions.checkPrimeNumber(i):
            lst.append(i)
    return lst


n = int(input())
print(solution(n))
