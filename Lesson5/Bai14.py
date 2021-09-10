# // Nhập 2 số nguyên dương n và k (k<=n). Tính nCk = n!/(k!*(n-k)!)
def checkValid(n, k):
    if n >= k:
        return True
    return False


def solution(n, k, flag):
    if flag:
        result = 1
        for i in range(1, n + 1):
            if i <= k:
                result *= 1 / i
            if i > n - k:
                result *= i
        return result
    return -1


n = int(input())
k = int(input())
flag = checkValid(n, k)
result = solution(n, k, flag)
print(result if flag else "Không tính được")
