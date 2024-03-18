num1, num2 = tuple(map(int, input().split()))

def calNume(num1, num2):
    a = 0
    b = 0

    if num1 > num2:
        a = num1
        b = num2
    else: 
        b = num1
        a = num2


    a += 25
    b *= 2

    num1 = b
    num2 = a

    return num1 , num2

num1, num2 = calNume(num1, num2)

print(num1, num2)