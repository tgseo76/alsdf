## normal.sy
```python
arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr,st,en):
    if st>=en: # 리스트에 원소가 1개 인경우 탈출 조건
        return

    pivot=st
    left=st+1
    right=en

    while(left<=right): # 엇갈리면 종료
        while(left<=en and arr[left]<=arr[pivot]): # 왼쪽에서부터 피벗보다 큰 값 찾기
            left+=1
        while(right>st and arr[right]>=arr[pivot]):# 오른쪽에서부터 피벗보다 작은 값 찾기
            right-=1

        if(left>right): #엇갈리면 스왑
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else: # 엇갈리지 않았으면 스왑
            arr[left],arr[right]=arr[right],arr[left]

    quick_sort(arr,st,right-1) # 분할 후 왼쪽부분 
    quick_sort(arr,right+1,en) # 분할 후 오른쪽 부분

quick_sort(arr,0,len(arr)-1)
print(arr) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
## py.st
```python
arr=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```