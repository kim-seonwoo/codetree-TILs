A = input()


# 문자열에 알파벳이 2개 이상인지 여부를 반환합니다.
def is_more_twoalp(string):
    # 하나라도 서로 다른 알파벳이 있다면
    # 그 문자열은 알파벳이 2개 이상입니다.
    leng = len(string)
    for i in range(leng):
        if string[i] != string[0]:
            return True
    
    return False


if is_more_twoalp(A):
    print("Yes")
else:
    print("No")