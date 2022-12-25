'''
https://www.acmicpc.net/problem/1316
3
happy
new
year

3

4
aba
abab
abcabc
a

1
'''


n=int(input())
cnt=0

for i in range(n):
    i=str(input())
    err=0
    chk = []

    for k in range(len(i)-1):
        chk.append(i[0])

        if i[k]!=i[k+1]:
            if i[k+1] in chk:
                err+=1
                break
            else:
                chk.append(i[k+1])
    if err==0:
        cnt+=1

print(cnt)






