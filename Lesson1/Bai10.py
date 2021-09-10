# //Nhập một số thực a. Xuất ra số nguyên lớn nhất nhưng nhỏ hơn a.
# //Ví dụ: a = 3.2 thì xuất 3. a=5 thì xuất 4).
def solution(a):
    if(a - int(a) > 0 ):
        return int(a)
    return int(a) -1

a = float(input())
print(solution(a))