'''
https://www.acmicpc.net/problem/2178

4 6
101111
101010
101011
111011
'''
import sys
from collections import deque

n,m=list(map(int,input().split()))
graph=[]

for i in range(n):
    i=list(map(int,input()))
    graph.append(i)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        a,b=q.popleft()

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[a][b]+1
                q.append((nx,ny))
    return graph[n-1][m-1]


print(bfs(0,0))