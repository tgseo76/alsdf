'''
https://school.programmers.co.kr/learn/courses/30/lessons/42862

n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''

def solution(n, lost, reserve):
    arr = [1] * (n + 2)
    answer = 0
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1

    print(arr)

    for i in range(1, n + 1):
        if arr[i] > 1:
            if (arr[i - 1] == 0):
                arr[i] -= 1
                arr[i - 1] += 1
            elif (arr[i + 1] == 0):
                arr[i] -= 1
                arr[i + 1] += 1
    print(arr)

    for i in range(1, n + 1):
        if (arr[i] > 0):
            answer += 1
    return answer


n=3
lost=[3]
reserve=[1]

arr=[1]*(n+2)
answer=0
for i in lost:
    arr[i]-=1
for i in reserve:
    arr[i]+=1

print(arr)

for i in range(1,n+1):
    if arr[i]>1:
        if(arr[i-1]==0):
            arr[i]-=1
            arr[i-1]+=1
        elif(arr[i+1]==0):
            arr[i]-=1
            arr[i+1]+=1
print(arr)

for i in range(1,n+1):
    if(arr[i]>0):
        answer+=1
print(answer)

477584
877544



