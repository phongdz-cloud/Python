# // Nhập vào số nguyên dương n. Tính tổng các ước số của n
def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum


n = int(input())
print(solution(n))
