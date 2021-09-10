# // Nhập số nguyên dương n. Tính S = 1^2 + 2^2 + ... + 2^n
import myfuntions as f


def solution(n, lst):
    sum = 0
    for i in range(0, n + 1):
        sum += i * i
    return sum


n = int(input())
lst = f.myInput(n)
print(solution(n, lst))
