# // Nhập vào số nguyên dương n. Tính tổng các chữ số của n
import math


def solution(n):
    sum = 0
    while n > 0:
        temp = n % 10
        n /= 10
        n = math.floor(n)
        sum += temp
    return sum


n = int(input())
print(solution(n))
