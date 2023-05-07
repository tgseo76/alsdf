'''
https://www.acmicpc.net/problem/2798

5 21
5 6 7 8 9

21
'''
from itertools import combinations
n=list(map(int,input().split()))
a=list(map(int, input().split()))
sum_c=0
for i in combinations(a,3):
    if sum(i)>n[1]:
        continue
    else:
        if sum_c<sum(i):
            sum_c=sum(i)

print(sum_c)

#
# n=list(map(int,input().split()))
# a=list(map(int, input().split()))
# c_sum=[]
# for i in range(0,n[0]):
#     for j in range(i+1,n[0]):
#         for k in range(j+1,n[0]):
#              if a[i] + a[j] + a[k] > n[1]:
#                  continue
#              else:
#                  c_sum.append(a[i] + a[j] + a[k])
#
# print(max(c_sum))