n = int(input())
list_num = tuple(map(int, input().split()))
dp = []
count = 1

def calList(index):
    global count

    if index == n:
        return

    if list_num[index] > dp[-1]:
        dp.append(list_num[index])
        count += 1
        calList(index + 1)

dp.append(list_num[0])
calList(1)

print(count + 1)