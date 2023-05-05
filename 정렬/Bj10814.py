'''
https://www.acmicpc.net/problem/10814

3
21 Junkyu
21 Dohyun
20 Sunyoung

20 Sunyoung
21 Junkyu
21 Dohyun
'''


t=int(input())
g_list=[]
for _ in range(t):
    age,name=list(map(str, input().split()))
    age=int(age)
    g_list.append((age,name))

g_list.sort(key=lambda x:x[0])

for _ in g_list:
    print(*_,sep=' ')