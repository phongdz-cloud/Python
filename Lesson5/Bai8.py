# //Tìm ước số lẻ lớn nhất của số nguyên dương n
def solution(n):
    max = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0 and i > max:
            max = i
    return max

n = int(input())
print(solution(n))