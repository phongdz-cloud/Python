# /*
#    Tìm "hoàn thiện cuối cùng" trong mảng một chiều các số nguyên. Nếu mảng không có
#    số hoàn thiện thì trả về -1;
# */
import myfuntions


def solution(n, lst):
    findLastPerfectNumber = -1
    for i in range(0, n):
        if myfuntions.checkPerfectNumber(lst[i]):
            findLastPerfectNumber = lst[i]
    return findLastPerfectNumber


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
