# /*
#   Viết chương trình kiểm tra xem số lượng số nguyên tố và số hoàn hảo trong mảng
#   có bằng nhau hay không
# */
import myfuntions


def solution(n, lst):
    numberPerfect = numberPrimer = 0
    for i in range(0, n):
        if myfuntions.checkPerfectNumber(lst[i]):
            numberPerfect += 1
        if myfuntions.checkPrimeNumber(lst[i]):
            numberPrimer += 1
    return numberPerfect == numberPrimer


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n,lst))
