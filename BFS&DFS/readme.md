### dfs(깊이우선)
```python
1. 그래프 n,m확인
2. def dfs:
    1. 범위 밖 False
    2. 방문확인
    3. nx,ny 
       def(nx,ny):
           return True
```

### bfs(너비우선)
```python
from collections import deque
1. 큐 생성
2. q.append((x,y))
3.그래프 방문처리
4. while문
    1.x,y = pop
    2.범위밖,벽인경우  continue
    3.큐 추가
    4. 처음반문하는 경우 거리기록
```