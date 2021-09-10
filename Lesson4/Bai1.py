# //Nhập vào số nguyên n. Cho biết n có phải là số chính phương hay không?
# // VD: 4,9,16
import myfuntions

n = int(input())
flag = myfuntions.checkSquareNumber(n)
print("n là số chính phương" if flag else "n không phải là số chính phương")
