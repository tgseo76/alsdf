# 소수찾기 문제


 def solution(n):
     arr = [True]*(n+1)
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

