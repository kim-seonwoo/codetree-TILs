n = int(input())
arr = list(map(int, input().split()))


# n을 n의 절대값으로 변경합니다.
def absolute_value(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]
    
    return


absolute_value(arr)


for elem in arr:
    print(elem, end=" ")