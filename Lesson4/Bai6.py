# //Nhập vào số nguyên. Cho biết n có bao nhiêu chữ số là số nguyên tố
import myfuntions
import math


def findPrimeNumber(n):
    count = 0
    while n > 0:
        if myfuntions.checkPrimeNumber(n % 10):
            count += 1
        n = math.floor(n / 10)
    return count


n = int(input())
print(findPrimeNumber(n))
