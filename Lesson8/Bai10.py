# /*
#     Tìm "số hoàn thiện nhỏ nhất" trong mảng một chiều các số nguyên. Nếu mảng không có
#     số hoàn thiện thì trả về số 0
# */
import myfuntions


def solution(n, lst):
    minPerfectNumber = 9999999
    for i in range(0, n):
        if myfuntions.checkPerfectNumber(lst[i]) and lst[i] < minPerfectNumber:
            minPerfectNumber = lst[i]
    return minPerfectNumber if minPerfectNumber != 9999999 else 0


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
