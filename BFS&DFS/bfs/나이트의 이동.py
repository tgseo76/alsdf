'''
https://www.acmicpc.net/problem/7562

3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''
from collections import deque
dx=[-2,-2,-1,1,2,2,-1,1]
dy=[-1,1,-2,-2,-1,1,2,2]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=1

    while q:
        a,b=q.popleft()

        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]

            if a==c and b==d:
                print(graph[a][b]-1)
                return True

            if nx<0 or ny<0 or nx>=l or ny>=l:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[a][b]+1
                q.append((nx,ny))
    return False


t=int(input())

for k in range(t):
    l = int(input())
    graph = []
    for i in range(l):
        _=[0]*l
        graph.append(_)

    a,b=list(map(int,input().split()))
    c,d=list(map(int,input().split()))
    bfs(a,b)

