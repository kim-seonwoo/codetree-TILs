num1, num2 = tuple(map(int, input().split()))
cnt = 0

def isSosu(num):
    for i in range(2, num):
        if num % (i) == 0:
            return False

    return True

for i in range(num1, num2+1):
    if isSosu(i):
        cnt += i


print(cnt)