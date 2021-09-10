# /*
#     Viết chương trình tính trung bình cộng của số chia hết cho 5
# */
import myfuntions
def solution(n,lst):
    sum = 0
    count = 0
    for i in range(0,n):
        if lst[i] % 5 ==0:
            sum += lst[i]
            count+=1
    if count!=0 :
        return sum/count
    return -1

n = int(input())
lst = myfuntions.myInput(n)
print(solution(n,lst))