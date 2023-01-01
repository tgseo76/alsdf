phone=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

str=input()
cnt=0
for i in range(len(str)):
    for j in phone:
        if(str[i] in j):
            cnt+=phone.index(j)+3

print(cnt)


