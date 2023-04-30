#230429

#11654번
#내가 시도한.....
# w = input()
# mydict={}
# a=48
# for i in range(10):
#     mydict[i] = a
#     a+=1
# b=65
# Alpha=['A','B','C','D','E']
# for i in range(25):

#ord() : 문자의 아스키 코드값을 리턴하는 함수이다.
#chr() : 아스키 코드값 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다.

# a = input()
# print(ord(a))

#2908번
# a,b=input().split()
# a=a[-1]+a[-2]+a[-3]
# b=b[-1]+b[-2]+b[-3]
# a=int(a)
# b=int(b)
# print(max(a,b))

#15552번
# import sys
# n =int(input())
# for i in range(n):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

#10162번
# n = int(input())
# a=300; b=60; c=10
# A=0; B=0; C=0
# no = False
# if n//a > 0:
#     A = n//a
#     n=n-(300*A)
# else:
#     A=0
# if n//b > 0:
#     B = n//b
#     n=n-(60*B)
# else:
#     B=0
# if n//c > 0 and n%c==0:
#     C = n//c    
# elif (A>0 or B>0) and n%c==0:
#     no = False
# else:
#     no = True
#     print(-1)
# if no == False:
#     print(A, end=' ')
#     print(B, end=' ')
#     print(C, end=' ')

#5618번 - 실패
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
#         if a%i==0 and b%i==0:
#             print(i)
