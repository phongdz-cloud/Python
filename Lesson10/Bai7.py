# /*
#     Viết hàm trích ra n ký tự đầu tiên/ cuối cùng bắt đầu từ vị trí pos
# */

def subStrHead(s,index):
    return s[0:index:]
def subStrLast(s,index):
    return s[index-1::]
def subStrPosition(s,n,index):
    return s[index:n+1]

s = input()
n = int(input())
index = int(input())
print(subStrPosition(s,n,index))