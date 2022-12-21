# py
```python
입력 속도
import sys
input = sys.stdin.readline

파이썬 스왑
a,b=b,a  

파이썬
and : 논리 and연산
& : 비트연산
```
## 리스트
```python
괄호풀기
a=[1,2,3,4,5]
print(*a) # 1 2 3 4 5
print(*lst, sep = ',') ==> x,y,z

리스트복사 ==> copy()
list2 = list1.copy()
list2 = list(list1)
list2 = [] + list1
```
##  큐
```python
import sys
from collections import deque
q=deque(arr)
```
## 이진탐색
```python
# 함수이용, 딕셔너리&해시
1.target_list 정렬

2.탐색 함수
def search(st,en,tg):

if st==en:
//
return


mid =(st+en)//2

if nums[mid]<target:
    search(mid+1,en,tg)
else:
    search(st,mid,target)
```
## 재귀
```python
재귀함수 깊이 늘리기
import sys
sys.setrecursionlimit(10**9)
```
## 정렬
```python
arr1.sort() 오름차순 // 0 ,1 ,2 ,3,4
arr2.sort(reverse=True) 내림차순 5, 4 , 3 ,2,1

(key=lambda x: (x[1], x[0])) y축정렬후 x
g_list.sort(key=lambda x:x[1])   
==> (key=lambda x:x[1]) # = y좌표값 정렬 

g_list.sort(key=lambda x : len(x) )  =길이값비교
```
## dfs & bfs
```python
dfs(깊이 우선)
1. 그래프 n,m확인
2. def dfs:
    1. 범위 밖 False
    2. 방문확인
    3. nx,ny 
       def(nx,ny):
           return True
```
---
```python
bfs(너비우선)
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


