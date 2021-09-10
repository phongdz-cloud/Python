# // Nhập số nguyên dương n. Tính S = 1! + 2! + ... + n!

def solution(n):
    result = 0
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        result += temp
    return result


n = int(input())
print(solution(n))
