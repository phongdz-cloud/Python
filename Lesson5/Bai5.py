# //Liệt kê các số hoàn hảo nhỏ hơn n
import myfuntions


def solution(n):
    lst = []
    for i in range(1, n):
        if myfuntions.checkPerfectNumber(i):
            lst.append(i)
    return lst


n = int(input())
print(solution(n))
