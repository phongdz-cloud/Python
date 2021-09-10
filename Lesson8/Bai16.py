# /*
#    Cho mảng A có n phần tử. Viết chương trình minh họa các thao tác cập nhật
#    và xóa phần tử tại vị trí i trong mảng. Thực hiện việc
#    chèn thêm một số nguyên x sau phần tử i (0<=i<n)
# */
import myfuntions


def checkValid(n, index):
    return 0 <= index < n


def myUpdate(n, lst, index, k):
    if checkValid(n, index):
        lst[index] = k


def myDelete(n, lst, index):
    if checkValid(n, index):
        del lst[index]


def myInsert(lst, index, k):
    if checkValid(len(lst), index):
        lst.insert(index, k)


n = int(input())
lst = myfuntions.myInput(n)
index = int(input("Nhập vào vị trí muốn thêm: "))
k = int(input("Nhập vào giá trị muốn thêm: "))
# myDelete(n, lst, index)
myInsert(lst, index, k)
print(lst)
