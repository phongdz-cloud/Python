# /*
#     Phân tích n thành các thừa số nguyên tố
# */
import myfuntions
def solution(n):
    lst = []
    i = 2
    while n > 1:
        if n % i == 0 and myfuntions.checkPrimeNumber(i):
            n /= i
            lst.append(i)
        else:
            i+=1
    return lst

n = int(input())
print(solution(n))