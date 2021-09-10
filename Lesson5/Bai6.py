# //Đếm số lượng số chính phương nhỏ hơn n
import myfuntions


def solution(n):
    count = 0
    for i in range(1, n):
        if myfuntions.checkSquareNumber(i):
            count += 1
    return count


n = int(input())
print(solution(n))
