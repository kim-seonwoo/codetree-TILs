num1, num2 = tuple(map(int, input().split()))

def calNum(num1, num2):
    count = num1
    for i in range(num2-1):
        count = count * num1
    print(count)



calNum(num1, num2)