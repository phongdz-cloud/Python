import myfuntions

n = int(input())
flag = myfuntions.checkSymmeTryNumber(n)
print("N là số đối xứng" if flag else "N không phải là số đối xứng")
