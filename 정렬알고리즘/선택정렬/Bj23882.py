'''
https://www.acmicpc.net/problem/23882
5 2
3 1 2 5 4

2 1 3 4 5
'''

n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
cnt=0
for i in range(n-1,0,-1):
    idx=arr.index(max(arr[:i+1]))
    if arr[i]!=arr[idx]:
        cnt+=1
        arr[i],arr[idx]=arr[idx],arr[i] #파이썬 tmp안써도 가능
        if (cnt==k):
            print(*arr)
if (cnt<k):
    print(-1)

