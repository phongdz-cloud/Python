# // Nhập số nguyên dương n. Tính S = 1 + (1+2)/2! + (1+2+3)/3! + ... + (1+2+3 + ... +n)/n!
def solution(n):
    result = 0
    sum = 0
    mul = 1
    for i in range(1, n + 1):
        sum += i
        mul *= 1 / i
        result += sum * mul
    return result


n = int(input())
print(solution(n))
