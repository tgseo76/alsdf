'''
https://www.acmicpc.net/problem/2667
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
from collections import deque
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    global house
    q=deque()
    q.append((x,y))
    house+=1
    graph[x][y]=0

    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]

            if(nx<0 or ny<0 or nx>=n or ny>=n):
                continue
            if(graph[nx][ny]==0):
                continue

            if(graph[nx][ny]==1):
                house+=1
                graph[nx][ny]=0
                q.append((nx,ny))




n=int(input())
cnt=0
house=0
dap=[]
graph=[] #[[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
for i in range(n):
    i=list(map(int,input().strip()))
    graph.append(i)

for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            bfs(i,j)
            cnt+=1
            dap.append(house)
            house=0
dap.sort()
print(cnt)
for i in dap:
    print(i)


