# /*
#     Kiểm tra mảng số nguyên có tồn tại giá trị 0 hay không? Nếu không tồn tại giá trị 0 thì trả vể giá trị 0
#     , ngược lại trả về 1
# */
import myfuntions


def checkZero(n, lst):
    for i in range(0, n):
        if lst[i] == 0:
            return 1
    return 0


n = int(input())
lst = myfuntions.myInput(n)
print(checkZero(n, lst))
