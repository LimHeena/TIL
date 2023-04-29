#230424

#1712번 - 이렇게 풀면 시간초과
# a,b,c = map(int, input().split())
# num = 1
# if b >= c:
#     print(-1)
# else:
#     while True:
#         if a + b*num < c*num:
#             break
#         else:
#             num += 1
#     print(num)
#정답
# a,b,c = map(int, input().split())
# if b >= c:
#     print(-1)
# else:
#     print(a//(c-b)+1)

#17614번
# num = int(input())
# ct = 0
# for i in range(1, num+1):
#     for j in str(i):
#         if j =='3' or j == '6' or j == '9':
#             ct += 1
# print(ct)

#2884번
# h,m = map(int, input().split())
# m = m-45
# if m < 0:
#     m = 60+m
#     h = h-1
#     if h < 0:
#         h = 24+h
# print(h, m)

#2444번
# n = int(input())
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))
# for j in range(n-1,0,-1):
#     print(' '*(n-j)+'*'*(2*j-1))

#2908번
# a,b = map(str, input().split())
# a = a[-1]+a[-2]+a[-3]
# b = b[-1]+b[-2]+b[-3]
# a = int(a)
# b = int(b)
# print(max(a,b))

#3040번 
#브루트포스 알고리즘
# mylist=[]
# for i in range(9):
#     mylist.append(int(input()))
# for j in range(9):
#     for k in range(j+1, 9):
#         if sum(mylist) - mylist[j] - mylist[k] == 100:
#             a,b = j,k
#             break
# mylist.pop(a)
# mylist.pop(b-1)
# for i in range(7):
#     print(mylist[i])