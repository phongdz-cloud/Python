# // Nhập 3 số nguyên a, b,  và n với a,b <n. Tính tổng các số nguyên dương nhỏ hơn n chia hết cho a nhưng không
# // chia hết cho b

def flagCheckNumber(a, b, n):
    if a < n and b < n:
        return True
    return False


def solution(a, b, n):
    sum = 0
    for i in range(1, n):
        if i % a == 0 and i % b != 0:
            sum += i
    return sum


a = int(input())
b = int(input())
n = int(input())
flag = flagCheckNumber(a, b, n)
result = solution(a, b, n)
print(result if flag else "A hoặc B lớn hơn N")
