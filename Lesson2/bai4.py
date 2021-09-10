# //Nhập vào tháng và năm. Cho biết tháng đó có bao nhiêu ngày
# /*
#  Tháng 1: 31
#  Tháng 2 : 28 hoặc 29
#  Tháng 3: 31
#  Tháng 4: 30
#  Tháng 5: 31
#  Tháng 6: 30
#  Tháng 7: 31
#  Tháng 8: 31
#  Tháng 9: 30
#  Tháng 10: 31
#  Tháng 11: 30
#  Tháng 12: 31
# */
import myfuntions as f
def solution(days,m,flag):
    return days[0] if (m == 2 and flag == True) else days[m]

days = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = int(input())
y = int(input())
flag = f.checkLeapYear(y)
print(solution(days,m,flag))