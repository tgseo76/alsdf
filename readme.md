# py

```python
import math

입력
속도
import sys

input = sys.stdin.readline

파이썬
스왑
a, b = b, a

파이썬
and: 논리
and연산
&: 비트연산

슬라이싱
arr[start: end: step]
arr = arr[start: end: step]

>> > a = ['a', 'b', 'c', 'd', 'e']
>> > a[1:]
['b', 'c', 'd', 'e']

>> > a[-3:]
['c', 'd', 'e']

제곱(pow),제곱근(sqrt)
math.pow(x,y) ==> x의 y제곱 math.pow(12,2) ==> 144.0

math.sqrt(x) ==> x의 제곱근 math.sqrt(121) ==> 11.0  

문자열 출력
김서방은 1에 있다 ==> "김서방은 "+cnt+"에 있다" ==> 오류
answer = "김서방은 " + str(cnt) + "에 있다" ==> 서방은 1에 있다

"김서방은 {}에 있다".format(cnt) ==> 김서방은 1에 있다.


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

리스트로
12345 = > [1,2,3,4,5]
==> n=list(map(int,input().strip()))

n=list(map(int,str(n))) ==> [1,2,3,4,5]

리스트 reverse
[1,2,3,4,5] => [5,4,3,2,1]
==> 
n.reverse() => print(n) ==> [5,4,3,2,1]

n=reversed(n) => print() ==> <list_reverseiterator object at 0x000002EFE79E9300>
==> print(list(n)) ==> [5,4,3,2,1]

리스트 합치기
s= ['1', '2', '3', '4', '5']
s1="".join(s) ==> 12345 (str) 

s1="_".join(s) ==> 1_2_3_4_5

리스트 차집합
ListA = [10,9,8,7,6,5,4,3,2,1] # 자연수
ListB = [1,3,5,7,9] # 홀수

ListC = [x for x in ListA if x not in ListB] # ListB에 포함되어 있지 않을 때만 ListA의 원소를 추가 ==> ListC: [10, 8, 6, 4, 2]
ListD = list(set(ListA) - set(ListB)) # 집합으로 만들어 빼기 ==> ListD: [2, 4, 6, 8, 10]



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

sort & sorted()
dap.sort() ==> dap이 바로 정렬됨
sorted(dap) ==> dap은 변화가 없음 =>print(sorted(dap)) 리턴값으로 정렬


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


