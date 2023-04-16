#230416

#3009번
# x = []
# y = []
# for i in range(3):
#     a,b = map(int, input().split())
#     x.append(a)
#     y.append(b)
# for i in range(3):
#     if x.count(x[i]) == 1:
#         x_re = x[i]
#     if y.count(y[i]) == 1:
#         y_re = y[i]
# print(x_re, y_re)

#1085번
# x,y,w,h = map(int, input().split())
# print(min(x,y,w-x,h-y))

#4153번
# import math
# while True:
#     a,b,c=map(int, input().split())
#     if a==0 and b==0 and c==0:
#         break
#     mylist = [a,b,c]
#     mylist.sort(reverse=True)
#     if mylist[0] == math.sqrt((pow(mylist[1],2)+pow(mylist[2],2))):
#         print('right')
#     else:
#         print('wrong')

#3053번
# import math
# R = int(input())
# print(pow(R,2)*math.pi)
# print(2*R*R)

#10250번
# T = int(input())
# for i in range(T):
#     H,W,N = map(int, input().split())
#     #H:층 수 W:각 층 방 수 N: 몇번째 고객
#     floor = N % H
#     num = (N//H)+1
#     if floor ==0:
#         floor = H
#         num -=1
#     print(floor * 100 + num)

#10872번
# n = int(input())
# sum=1
# for i in range(1, n+1):
#     sum *= i
# print(sum)    

#2562번
# mylist =[]
# for i in range(9):
#     mylist.append(int(input()))
# max=1
# idx=-1
# for i in range(len(mylist)):
#     if max < mylist[i]:
#         idx=i+1
#         max = mylist[i]
# print(max)  
# print(idx)      

#2577번
# a=[]
# for i in range(3):
#     a.append(int(input()))
# num = str(a[0]*a[1]*a[2])
# for i in range(10):
#     print(num.count(str(i)), end='\n')

#3052번
# a=[]
# for i in range(10):
#     a.append(int(input()))
# b=[]
# for i in range(10):
#     b.append(int(a[i]%42))
# myset=set(b)
# mylist = list(myset)
# print(len(mylist))

#8958번
# T = int(input())
# for i in range(T):
#     myinput = input()
#     plus = 0
#     score = 0
#     for i in range(len(myinput)):
#         if myinput[i] == 'O':
#             plus += 1
#             score += plus 
#         else:
#             plus = 0
#     print(score)