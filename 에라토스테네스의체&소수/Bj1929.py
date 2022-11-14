'''
https://www.acmicpc.net/problem/1929
3 16

3
5
7
11
13
'''
import math

m,n=list(map(int, input().split()))

for i in range(m,n+1):
    cnt=0

    if i>1:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                cnt+=1
                break

        if cnt==0:
            print(i)
#32952	5628



#
# arr=[True]*(n+1)
# arr[0]=arr[1]=False
# cnt=0
# for i in range(2,int(math.sqrt(n))+1):
#     if arr[i]==True:
#         for j in range(2*i,n+1,i):
#             arr[j]=False
#
#
# for i in range(m,n+1):
#     if arr[i]==True:
#         print(i)

# 40628kb  356ms
