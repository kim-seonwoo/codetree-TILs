num = int(input())

def calYear(num):
    if num % 4 == 0:
        if num % 100 == 0 and num % 400 != 0:
            return False

        return True

    return False




if calYear(num):
    print("true")
else:
    print("false")