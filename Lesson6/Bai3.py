# /*
#     viết chương trình tính trung bình cộng của một mảng số nguyên N
# */
import  myfuntions
def solution(n,lst):
    sum = 0
    for i in range(0,n):
        sum += lst[i]
    return sum/n

n = int(input())
lst = myfuntions.myInput(n)
print(solution(n,lst))