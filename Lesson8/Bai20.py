# /*
#     Viết chương trình nhập vào một mảng, trong quá trình nhập,
#     mảng được sắp xếp thứ tự luôn (tăng / giảm)
# */

def solution(n):
    lst = []
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
        lst.sort()
    return lst


n = int(input())
print(solution(n))
