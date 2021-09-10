# /*
#     Viết chương trình nhập vào một dãy số A gồm m số thực
#     , nhập vào dãy số B gồm n số thực In ra các phần tử
#     chỉ xuất hiện trong dãy A mà không xuất hiện trong dãy B
# */
import myfuntions


def solution(lstA, lstB):
    lstC = []
    for i in range(0, len(lstA)):
        if lstA[i] not in lstB:
            lstC.append(lstA[i])
    return lstC


n = int(input("Nhập vào số lượng phân tử A: "))
lstA = myfuntions.myInputFloat(n)
m = int(input("Nhập vào số lượng phân tử B: "))
lstB = myfuntions.myInputFloat(m)
print(solution(lstA, lstB))
