# 소수찾기 문제

``` python
 def solution(n):
     arr = [True]*(n+1) ==> [True for i in range(n+1)]
     cnt=0
     for i in range(2,int(math.sqrt(n))+1):
         if arr[i]==True:
             for j in range(2*i,n+1,i):
                 arr[j]=False

#     소수의 갯수
#     cnt=arr.count(True)-2 #0,1은 소수가 아니라서 -2
#     return cnt

#    소수 출력
#    for i in range(2,len(arr+1):
#         print(i,end=' ')



l_cnt=0

for i in k:
    cnt=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
        if cnt==0:
            l_cnt+=1
```
bj1929=소수구하기
bj4948=베르트랑공준 (에라토스테네스의체)
bj9020=골드바흐의추측 (에라토스테네스의체)