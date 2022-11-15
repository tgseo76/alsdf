'''
https://www.acmicpc.net/problem/9020

3
8
10
16

3 5
5 5
5 11
'''
import math

t=int(input())

for _ in range(t):
    n=int(input())

    arr=[True]*(n+1)
    arr[0]=arr[1]=False

    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==True:
            for j in range(2*i,n+1,i):
                arr[j]=False
        # arr이 len(arr)을 대칭으로 l+r ==n && 좌우가 T
        # 8
        # [False, False, True, True, False, True, False, True, False]
        # 10
        # [False, False, True, True, False, True, False, True, False, False, False]
        # 16
        # [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False]

        l = int((len(arr)/2))
        r = int((len(arr)/2))
    while(1):
        if((arr[l] and arr[r]) and l+r==n):
            print(l,r)
            break
        else:
            l-=1
            r+=1