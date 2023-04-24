'''
https://school.programmers.co.kr/learn/courses/30/lessons/42895

n=5 number=12 return 4
n=2 number=11 return 3
'''


def solution(N, number):
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1,9):
        dp[i].append(int(str(N)*i))
        for j in range(1,i):
            for front in dp[j]:
                for back in dp[i-j]:
                    dp[i].append(front+back)
                    dp[i].append(front-back)
                    dp[i].append(front*back)
                    if back:
                        dp[i].append(front//back)
        dp[i] = list(set(dp[i]))
        if number in dp[i]:
            answer = i
            break
    return answer

'''
N=5
number=12
for i in range(1,9):
    dp[i].append(int(str(N)*i))
    for j in range(1,i):
        for front in dp[j]:
            for back in dp[i-j]:
                dp[i].append(front+back)
                dp[i].append(front-back)
                dp[i].append(front*back)
                if back:
                    dp[i].append(front//back)
    dp[i] = list(set(dp[i]))
    if number in dp[i]:
        answer = i

print(i)
'''