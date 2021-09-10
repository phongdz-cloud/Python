# //Nhập vào một số thực. làm tròn số thực này thành số nguyên theo nguyên tắc làm tròn thông thường
# //(phần lẻ >=0.5 thì làm tròn lên)
def solution(a):
    b = int(a)
    if( a < 0 and a + b * (-1) < -0.5):
        return b-1
    if(a - b >= 0.5):
        return b +1
    return b

a = float(input())
print(solution(a))