# // Nhập vào 2 số nguyên a,b. Tìm nghiệm phương trình ax+b=0;
def solution(a,b):
    if(a == 0):
        return True
    return -b/a
def output(result, b):
    if(result == True):
        print("Phương trình vô số nghiệm" if b == 0 else
              "Phương trình vô nghiệm")
    else:
        print(result)
a = int(input())
b = int(input())
result = solution(a,b)
output(result,b)
