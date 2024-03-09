num = int(input())

def calYear(num):
    if num % 4 == 0:
        return True

    elif num % 100 == 0 and num % 400 != 0:
        return True


if calYear(num):
    print("true")
else:
    print("false")