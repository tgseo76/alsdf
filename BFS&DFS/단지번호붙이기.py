'''
https://www.acmicpc.net/problem/2667
'''
# DFS

def dfs(x,y):
    global house
    dx=[0,0,1,-1]
    dy=[-1,1,0,0]

    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y]==0:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        house+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        return True

n=int(input())
graph=[]
house=0
dap=[]
cnt=0
for i in range(n):
    i=list(map(int,input().strip()))
    graph.append(i)

for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            dfs(i,j)
            dap.append(house)
            house=0
            cnt+=1

dap.sort()
print(cnt)
for i in dap:
    print(i)




