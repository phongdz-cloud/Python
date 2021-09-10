# /*
#     Cho mảng A có n phần tử đã có thứ tự tăng dần và một phần tử x.
#     Thực hiện chèn x vào mảng sao cho đảm bảo mảng vẫn có thứ tự tăng dần
# */
import myfuntions


def solution(lst, x):
    if lst[0] > x:
        lst.insert(0, x)
        return
    for i in range(0, len(lst) - 1):
        if lst[i] <= x <= lst[i + 1]:
            lst.insert(i + 1, x)
            return
    lst.push(x)


n = int(input())
lst = myfuntions.myInput(n)
x = int(input("Nhập vào giá trị muốn thêm"))
lst.sort()
print(lst)
solution(lst, x)
print(lst)
