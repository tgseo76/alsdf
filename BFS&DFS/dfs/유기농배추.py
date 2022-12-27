'''
https://www.acmicpc.net/problem/1012

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

5
1
'''
import sys
sys.setrecursionlimit(10**9)
t=int(input())


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        for _ in range(4):
            nx=x+dx[_]
            ny=y+dy[_]
            dfs(nx,ny)
        return True

for _ in range(t):
    cnt = 0
    n,m,k=list(map(int,input().split()))
    graph=[]
    for _ in range(n):
        graph.append([0]*m)

    for _ in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                cnt+=1
    print(cnt)













