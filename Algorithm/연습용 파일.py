# 2주차 1

# my = list(map(int,input().split()))
# my.sort()
# print(my[2]+my[3]-my[0]-my[1])

# 2주차 2

# n = int(input())
# my = list(map(int, input().split()))
# print(oct(sum(my))[2:])

# 2주차 3

# def prime(N):
# 	is_prime = [1 for _ in range(N+1)] # 초기에는 다 소수로 지정.
# 	prime = [] # 찐 소수인 리스트.
# 	for i in range(2, N+1): # 2부터 N까지 범위.
# 		if not is_prime[i]: # 소수가 아닌 것들은 제외
# 			continue
# 		prime.append(i) # 찐 소수에 넣기
# 		for j in range(i*2, N+1, i): # 그 소수의 배수도 제외
# 			is_prime[j] = 0
# 	return prime

# n = int(input())
# my = list(map(int, input().split()))
# my = [0]+ my
# ans = 0
# prime = prime(n)
# for k in prime:
# 	ans += my[k]
	
# print(ans)