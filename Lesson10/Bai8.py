# /*
#     Viết chương trình kiểm tra một chuỗi có phải là chuỗi con
#     của chuỗi kia hay không
# */
def solution(s1,s2):
    return s1 in s2
s1 = input()
s2 = input()
print(solution(s1,s2))