# /*
#     Cho 2 mảng A,B có thứ tự tăng dần. Thực hiện việc trộn 2 mảng A và B
#     để tạo ra mảng cũng có thứ tự tăng dần
# */
import myfuntions


def checkIndex(lst, x):
    for i in range(0, len(lst)-1):
        if lst[i] <= x <= lst[i + 1]:
            return i + 1
    return len(lst)


def mergeArray(lstA, lstB):
    lstC = []
    if lstA[0] > lstB[0]:
        temp = lstA[0]
        lstA[0] = lstB[0]
        lstB[0] = temp
    lstC.append(lstA[0])
    lstC.append(lstB[0])
    for i in range(0, len(lstA)):
        lstC.insert(checkIndex(lstC, lstA[i]), lstA[i])
        lstC.insert(checkIndex(lstC, lstB[i]), lstB[i])
    return lstC


n = int(input("Nhập vào số lượng phần tử mảng A"))
lstA = myfuntions.myInput(n)
lstB = myfuntions.myInput(n)
lstA.sort()
lstB.sort()
print(mergeArray(lstA,lstB))
