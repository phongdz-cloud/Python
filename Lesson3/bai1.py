# // Nhập số nguyên dương n. Tính S = 1 +2 +3 + ... +n
import myfuntions as my


def solution(n, lst):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum


n = int(input())
lst = my.myInput(n)
print(solution(n, lst))
