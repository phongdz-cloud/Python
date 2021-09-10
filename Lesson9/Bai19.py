# // Cho mảng A gồm có n phần tử. Viết chương trình tìm số lớn thứ hai trong mảng.
# // lưu ý, chỉ duyệt mảng một lần
import myfuntions


def findMaxSecondArray(A):
    max = A[0]
    maxSecond = -9999999
    for i in range(0, len(A)):
        if A[i] > max:
            maxSecond = max
            max = A[i]
        if maxSecond < A[i] < max:
            maxSecond = A[i]
    return maxSecond if maxSecond != -9999999 else -1


n = int(input())
A = myfuntions.myInput(n)
result = findMaxSecondArray(A)
print(result if result != -1 else "Không có số lớn nhì")
