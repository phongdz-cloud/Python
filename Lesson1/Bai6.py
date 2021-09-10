def solution(h,m,s):
    if (h>= 0 and s >= 0 and m >=0):
        if(h <24 and m <60 and s < 60):
            return True
    return False

h = int(input())
m = int(input())
s = int(input())
print("Valid" if solution(h,m,s) else "Invalid")