'''
https://www.acmicpc.net/problem/4948

1
10
13
100
1000
10000
100000

0
1
4
3
21
135
1033
8392
'''


while(True):
    cnt=0
    n=int(input())
    if (n == 0):
        break
    arr=[True]*((2*n)+1)
    arr[0]=arr[1]=False

    for i in range(2,(2*n)+1):
        if arr[i]==True:
            for j in range(2*i,(2*n)+1,i):
                arr[j]=False


    for i in range(n+1,(2*n)+1):
        if (arr[i]==True):
            cnt+=1

    print(cnt)

    # 34716kb  4348ms










