str1 = input()
str2 = input()
count = 0

for i in range(len(str1)):
    if str1 == str2:
        print(count)
        exit()
        break
        

    str1 = str1[-1] + str1[:-1]
    count += 1


print(-1)

