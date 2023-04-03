#230331

#2739번

# N = int(input())
# for i in range(1,10):
#     print(f'{N} * {i} = {N*i}')
    
#10430번

# A,B,C = map(int, input().split())

# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

#9498번

# T = int(input())
# if 90 <= T <= 100:
#     print('A')
# elif 80 <= T <= 89:
#     print('B')
# elif 70 <= T <= 79:
#     print('C')
# elif 60 <= T <= 69:
#     print('D')
# else:
#     print('F')
    
#14681번

# x = int(input())
# y = int(input()) 

# if x>0 and y>0:
#     print('1')
# elif x<0 and y>0:
#     print('2')
# elif x<0 and y<0:
#     print('3')
# else:
#     print('4')

#2753번

# y = int(input())
# if y%4==0 and y%100!=0:
#     print('1')
# elif y%400==0:
#     print('1')
# else:
#     print('0')

#2438번

# N = int(input())
# for i in range(1,N+1):
#     print('*'*i)

#2439번

# N = int(input())
# for i in range(1,N+1):
#     print(' ' * (N-i) + '*' * i)

#2741번

# N = int(input())
# for i in range(1,N+1):
#     print(i)

#2742번

# N = int(input())
# for i in range(N,0,-1):
#     print(i)

#11022번

# case_num = int(input())
# for i in range(case_num):
#     A,B = map(int, input().split())
#     print(f"Case #{i+1}: {A} + {B} = {A+B}")

#8393번

# n = int(input())
# sum=0
# for i in range(1, n+1):
#     sum += i
# print(sum)

#10871번

# N,X = map(int, input().split())
# mylist = input().split()
# mylist = list(map(int, mylist))
    
# for i in range(len(mylist)):
#     if mylist[i] < X:
#         print(mylist[i], end=' ')


# N,X = map(int, input().split())
# mylist = list(map(int, input().split()))
    
# for i in range(len(mylist)):
#     if mylist[i] < X:
#         print(mylist[i], end=' ')
