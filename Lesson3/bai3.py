# // Nhập số nguyên dương n. Tính S = 1/1 + 1/2 + 1/3 + 1/n
import myfuntions as f


def solution(n, lst):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    return sum


n = int(input())
lst = f.myInput(n)
print(solution(n, lst))
