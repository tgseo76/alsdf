'''
https://www.acmicpc.net/problem/24091

5 1
2 5 1 4 3

2 5 1 4 3
--
5 2
2 5 1 4 3

2 1 5 4 3
--
5 10
2 5 1 4 3

-1
--
'''
a,k=list(map(int,input().split())) # a: arr크기 k:교환횟수
arr=list(map(int,input().split()))

cnt = 0
dap=[]
def quick_sort(arr,st,en):
    global cnt
    global dap
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

        if(left>right): #엇갈리면 스왑 [5,4,2,0,3,1,6,9,7,8] ==> [1,4,2,0,3,5,6,9,7,8]
            cnt += 1
            if(cnt==k):
                dap=arr.copy()
            arr[right],arr[pivot]=arr[pivot],arr[right]


        else: # 엇갈리지 않았으면 스왑 [5,7,9,0,3,1,6,2,4,8] ==> [5,4,9,0,3,1,6,2,7,8]
            cnt += 1
            if(cnt==k):
                dap = arr.copy()
            arr[left],arr[right]=arr[right],arr[left]

    quick_sort(arr,st,right-1) # 분할 후 왼쪽부분
    quick_sort(arr,right+1,en) # 분할 후 오른쪽 부분


quick_sort(arr,0,len(arr)-1)
if (len(dap)!=0):
    print(dap)
else:
    print(-1)
