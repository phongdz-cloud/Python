# //Nhập vào 2 số nguyên a, b. Xuất ra thương của 2 số nguyên (trường hợp b = 0 thì báo không chia được)
def solution(a,b):
    return a/b

a = int(input())
b = int(input())
print(solution(a,b) if b !=0 else "Infinity")