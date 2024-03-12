num = int(input())
arr = list(map(int,input().split()))

def calNum(arr):
    for i in range(num):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]// 2
    


calNum(arr)
for elem in arr:
    print(elem, end=" ")