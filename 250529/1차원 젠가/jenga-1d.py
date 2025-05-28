n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# 첫 번째 제거 구간 제거
temp = []
for i in range(0, s1 - 1):
    temp.append(blocks[i])
for i in range(e1, len(blocks)):
    temp.append(blocks[i])
blocks = temp

# 두 번째 제거 구간 제거
temp = []
for i in range(0, s2 - 1):
    temp.append(blocks[i])
for i in range(e2, len(blocks)):
    temp.append(blocks[i])
blocks = temp

# 출력
if not blocks:
    print(0)
else:
    for elem in blocks:
        print(elem)
