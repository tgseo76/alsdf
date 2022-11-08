'''
https://www.acmicpc.net/problem/1920

5
4 1 5 2 3
5
1 3 7 9 5

1 1 0 0 1
'''

m=int(input())
tg_l=list(map(int,input().split( )))
n=int(input())
arr=list(map(int,input().split( )))

tg_l.sort()

def bi(st,en,tg):
    if st==en:
        if tg_l[en]==tg:
            print(1)
        else:
            print(0)
        return

    mid=(st+en)//2

    if tg_l[mid]<tg:
        bi(mid+1,en,tg)
    else:
        bi(st,mid,tg)

for i in arr:
    bi(0,m-1,i)