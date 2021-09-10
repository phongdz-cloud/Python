# /*
#    Viết chương trình tính trung bình cộng các số nguyên tố trong mảng
# */
import myfuntions


def solution(n, lst):
    sum = count = 0
    for i in range(0, n):
        if myfuntions.checkPrimeNumber(lst[i]):
            count += 1
            sum += lst[i]
    return sum / count if count != 0 else "Không có số nguyên tố trong mảng"


n = int(input())
lst = myfuntions.myInput(n)
print((solution(n, lst)))
