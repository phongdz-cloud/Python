# //Liệt kê các số chính phương nhỏ hơn n
import myfuntions


def solution(n):
    lst = []
    for i in range(1, n):
        if myfuntions.checkSquareNumber(i):
            lst.append(i)
    return lst


n = int(input())
print(solution(n))
