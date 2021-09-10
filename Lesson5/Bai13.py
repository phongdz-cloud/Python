# // Nhập số nguyên n và số thực x Tính S = 1 + x/1 + x^2/2! + ... + x^n/n!
def solution(n, x):
    result = 1
    numerator = 1
    mul = 1
    for i in range(1, n + 1):
        numerator *= 1 / x
        mul *= 1 / i
        result += mul * (1 / numerator)
    return result


n = int(input())
x = int(input())
print(solution(n, x))
