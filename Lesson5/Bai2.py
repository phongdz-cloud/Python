# //Đếm số lượng số hoàn hảo nhỏ hơn n
import myfuntions


def solution(n):
    count = 0
    for i in range(1, n):
        if myfuntions.checkPerfectNumber(i):
            count += 1
    return count


n = int(input())
print(solution(n))
