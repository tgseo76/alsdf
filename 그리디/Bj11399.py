'''
https://www.acmicpc.net/problem/11399
5
3 1 4 3 2

32
'''
#
n=int(input())
p=list(map(int,input().split()))
dap=0
p.sort() #[1, 2, 3, 3, 4]
#1+(1+2)+(1+2+3)+(1+2+3+3)+(1+2+3+3+4)
for i in range(1,n+1):
    dap+=sum(p[0:i])

print(dap)



