# //Nhập vào số nguyên n. Cho biết n có phải là số nguyên tố hay không?
# // VD: 2,3,5,7
import  myfuntions

n = int(input())
flag = myfuntions.checkPrimeNumber(n)
print("N là số nguyên tố" if flag else "N không phải là số nguyên tố")
