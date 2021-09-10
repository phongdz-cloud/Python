# //Đếm xem n có bao nhiêu ước số là số nguyên tố
import myfuntions


def solution(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and myfuntions.checkPrimeNumber(i):
            count += 1
    return count


n = int(input())
print(solution(n))
