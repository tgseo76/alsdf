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

while(True):
    n=int(input())

    arr=[True]*(n+1)
    arr[0]=arr[1]=False

    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==True:
            for j in range(2*i,n+1,i):
                arr[j]=False




