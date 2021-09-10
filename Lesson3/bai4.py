# // Nhập số nguyên dương n. Tính S = 1*2*3*n!
import myfuntions as f


def solution(n, lst):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


n = int(input())
lst = f.myInput(n)
print(solution(n, lst))
