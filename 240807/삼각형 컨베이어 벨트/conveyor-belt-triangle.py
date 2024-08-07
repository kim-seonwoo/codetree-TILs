# 입력 받기
n, t = map(int, input().split())
belt1 = list(map(int, input().split()))
belt2 = list(map(int, input().split()))
belt3 = list(map(int, input().split()))

# 삼각형의 변들을 하나의 리스트로 연결
belt = belt1 + belt2 + belt3

# t초 만큼 회전
t = t % (3 * n)  # t가 3n의 배수일 경우 원래 상태로 돌아오므로
belt = belt[-t:] + belt[:-t]

# 결과를 다시 삼각형의 세 변으로 나누기
belt1 = belt[:n]
belt2 = belt[n:2*n]
belt3 = belt[2*n:]

# 결과 출력
print(' '.join(map(str, belt1)))
print(' '.join(map(str, belt2)))
print(' '.join(map(str, belt3)))