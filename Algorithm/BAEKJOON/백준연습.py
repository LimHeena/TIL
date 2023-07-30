#230430

#5618번 - 시간초과
# n = int(input())
# if n == 2:
#     a,b = map(int, input().split())
#     maxnum = max(a,b)
#     for i in range(1,maxnum+1):
#         if a%i==0 and b%i==0:
#             print(i)
# else:
#     a,b,c = map(int, input().split())
#     maxnum = max(a,b,c)
#     for i in range(1,maxnum+1):
#         if a%i==0 and b%i==0 and c%i==0:
#             print(i)

#두 수의 공약수 = 최대 공약수의 약수
#약수 구하기 함수
# from math import gcd, sqrt
# def div(n):
#     mylist=[]
#     for i in range(1,int(sqrt(n))+1):
#         if n%i==0:
#             mylist.append(i)
#             if i**2 != n:
#                 mylist.append(n//i)
#     mylist.sort()
#     return mylist

# num = int(input())
# if num ==2:
#     a,b = map(int, input().split())
#     mylist = div(gcd(a,b)) #최대공약수의 약수 
#     for i in range(len(mylist)):
#         print(mylist[i])
# else:
#     a,b,c = map(int, input().split())
#     mylist = div(gcd(a,b,c)) #최대공약수의 약수 
#     for i in range(len(mylist)):
#         print(mylist[i])
