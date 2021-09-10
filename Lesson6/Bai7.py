# /*
#     Viết chương trình xuất ra n phần tử đầu tiên cũa dãy fibonanci
# */
import myfuntions


def solution(n):
    lst = []
    for i in range(0, n):
        lst.append(fibo.fibonanci(i))
    return lst


n = int(input())
fibo = myfuntions.fibo(1, 1)
print(solution(n))
