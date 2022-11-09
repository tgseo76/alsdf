'''
https://www.acmicpc.net/problem/23881
K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 K 보다 작으면 -1을 출력한다.
5 2
3 1 2 5 4

2 3
'''
a,k=list(map(int,input().split()))
arr=list(map(int, input().split()))
cnt=0

for i in range(a-1,0,-1):
    tem=-1
    idx=arr.index(max(arr[:i+1]))
    if arr[idx]!=arr[i]:
        cnt+=1
        tem=arr[i]
        arr[i]=arr[idx]
        arr[idx]=tem
        if k==cnt:
            print(arr[idx],arr[i])
if cnt<k:
    print(-1)








