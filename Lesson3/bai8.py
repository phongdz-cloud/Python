# // Nhập vào số nguyên dương n. Xuất ra số ngược lại VD: Nhập 1706 -> 6071
import math


def solution(n):
    sum = 0
    while n > 0:
        temp = n % 10
        n /= 10
        n = math.floor(n)
        sum = sum * 10 + temp
    return sum


n = int(input())
print(solution(n))
