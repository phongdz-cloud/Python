# // Nhập số nguyên dương n, số thực x (x>0). Tính sqrt(x+(sqrt(x + ...sqrt(x))))
import math


def checkValid(n, k):
    if n > 0 and k > 0:
        return True
    return False


def solution(n, x, flag):
    if flag:
        sum = 0
        for i in range(1, n + 1):
            temp = sum + x
            sum = math.sqrt(temp)
        return sum
    return -1


n = int(input())
k = int(input())
flag = checkValid(n, k)
result = solution(n, k, flag)
print(result if flag else "Không tính được")
