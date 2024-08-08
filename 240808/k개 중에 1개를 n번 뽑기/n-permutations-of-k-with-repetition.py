k, m = tuple(map(int, input().split()))
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == m + 1:
        print_answer()
        return

    for i in range(k):
        answer.append(i + 1)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)