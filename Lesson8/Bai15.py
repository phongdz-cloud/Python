# /*
#    Cho mảng một chiều các số thực và một số thực x. Hãy viết hàm tìm giá trị
#    âm cuối cùng lớn hơn giá trị x. Nếu mảng không có giá trị thỏa
#    thì hàm trả về giá trị không chẵn là 0
# */
import myfuntions


def solution(n, lst, x):
    maxNegative = -999999
    for i in range(0, n):
        if 0 > lst[i] > maxNegative and lst[i] > x:
            maxNegative = lst[i]
    return maxNegative if maxNegative != -999999 else 0


n = int(input())
lst = myfuntions.myInputFloat(n)
x = float(input())
print(solution(n, lst, x))
