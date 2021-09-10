# //Nhập n in ra số đầu tiên trong dãy Fibonacci
import myfuntions


def solution(n):
    f = myfuntions.fibo(1,1)
    lst=[]
    for i in range(0, n):
        lst.append(f.fibonanci(i))
    return lst


n = int(input())
print(solution(n))
