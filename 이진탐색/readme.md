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
bj1920=수찾기  