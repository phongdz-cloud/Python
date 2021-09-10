# /*
#     Nhập vào một mảng số nguyên. Nhập tiếp một số nguyên x.
#     Cho biết vị trí cuối cùng(tính từ đầu mảng) mà x có trong mảng vừa nhập. Nếu không có x thì xuất -1;
# */
import myfuntions


def solution(n, x, lst):
    index = -1
    for i in range(0, n):
        if lst[i] == x:
            index = i
    return index


n = int(input())
x = int(input())
lst = myfuntions.myInput(n)
print(solution(n, x, lst))
