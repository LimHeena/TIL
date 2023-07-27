# 3주차 1

import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
print(sum(S))

# 3주차 2


answer = list(map(int, input()))
user_input = list(map(int, input()))

def fail():
    for i in range(4):
        if result[i] != 2:
            continue
        while True:
            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                break

def ball():
    if 1 not in result:
        return
    pos = []
    value = []
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])
    for i in range(len(pos)):
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]

make_input_count = 0
while True:
    make_input_count += 1
    result = [2, 2, 2, 2]
    if user_input == answer:
        print(make_input_count)
        break

    for i in range(4):
        if user_input[i] in answer:
            if user_input[i] == answer[i]:
                result[i] = 0
            else:
                result[i] = 1
                
    fail()
    ball()

# 3주차 3

N,K = map(int, input().split())
mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
cha_x = [-1,1,0,0]
cha_y = [0,0,1,-1]
for i in range(K):
	x, y = map(int, input().split())
	mat[x][y] += 1
	for j in range(4):
		nx, ny = x + cha_x[j], y + cha_y[j]
		if nx > N or nx < 1 or ny > N or ny < 1:
			continue
		mat[nx][ny] += 1
ans = 0
for k in range(1, N+1):
	for h in range(1, N+1):
		ans += mat[k][h]
print(ans)	