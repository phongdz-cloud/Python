# //Nhập vào số nguyên n.Tìm chữ số lớn nhất của n?
import math
def findMaxNumber(n):
    max = 0
    while n > 0:
        if n % 10 > max:
            max = n % 10
        n = math.floor(n / 10)
    return max

n = int(input())
print(findMaxNumber(n))