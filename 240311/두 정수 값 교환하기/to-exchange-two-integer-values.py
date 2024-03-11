num1, num2 = tuple(map(int, input().split()))


def calNum(a, b):
    num1 = b
    num2 = a
    return num1, num2

num1,num2 = calNum(num1, num2)

print(num1, num2)