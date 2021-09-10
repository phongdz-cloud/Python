# /*
#     Tìm giá trị âm đầu tiên trong mảng số thực. Nếu mảng không có giá trị âm thì trả về
#     giá trị không âm là giá trị 1
# */
import myfuntions


def solution(n, lst):
    for i in range(0, n):
        if lst[i] < 0:
            return lst[i]
    return 1


n = int(input())
lst = myfuntions.myInputFloat(n)
print(solution(n, lst))
