'''
https://school.programmers.co.kr/learn/courses/30/lessons/12909

"()()"

true
---
"(()("

false
'''

def solution(s):
    answer = True
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
            if cnt < 0:
                return False
    if cnt>0:
        return False
    return True

s="()()"
cnt = 0
for i in s:
    if i == "(":
        cnt += 1
    elif i == ")":
        cnt -= 1
        if cnt < 0:
            print("f")
if cnt > 0:
    print("f")

print(("t"))