'''
https://www.acmicpc.net/problem/1541

55-50+40

-35
---
00009-00009

0
'''


a=input().split("-")
dap=[]

for i in a:
    sum=0
    b=i.split("+")
    for j in b:
        sum+=int(j)
    dap.append(sum)

n=dap[0]

for i in range(1,len(dap)):
    n -=dap[i]
print(n)