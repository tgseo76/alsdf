'''
https://www.acmicpc.net/problem/2805

4 7
20 15 10 17

15

---
5 20
4 42 40 26 46


36

'''

def search(a,st,en):
    dap=0

    while st<=en:
        mid=(st+en)//2
        t=0

        for i in a:
            if i>mid:
                t+=i-mid


        if t<mid :
            en=mid-1
        else:
            dap = mid
            st = mid+1

    return dap

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))

dap=search(a,0,max(a))
print(dap)

