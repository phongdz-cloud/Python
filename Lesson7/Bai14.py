# /*
#   Kiểm tra mảng các số nguyên có toàn số chẵn hay không? Nếu có tồn tại giá trị lẻ trả về giá
#   0, ngược lại trả về giá trị 1
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n):
        if lst[i] % 2 != 0:
            return 0
    return 1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
