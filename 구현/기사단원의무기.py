'''
https://school.programmers.co.kr/learn/courses/30/lessons/136798

number	limit	power	result
5   	3	      2 	10
'''

import math

def solution(number, limit, power):
    arr = []
    answer=0

    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(math.sqrt(i))+1): #제곱근까지만
            if (i % j == 0):
                cnt += 1
                if (j ** 2 != i):  # 제곱근이면 +0 제곱근이 아니면 +1 ==> 2개씩 cnt++
                    cnt += 1
        arr.append(cnt)

    for i in range(len(arr)):
        if (arr[i] <= limit):
            pass
        else:
            arr[i] = power

    answer = sum(arr)
    return answer

number=10
limit=3
power=2

arr = []
answer = 0

for i in range(1, number + 1):
    cnt = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            cnt += 1
            if(j**2!=i):
                cnt+=1
    arr.append(cnt)
print(arr)

for i in range(len(arr)):
    if (arr[i] <= limit):
        pass
    else:
        arr[i] = power

answer = sum(arr)


