'''
https://school.programmers.co.kr/learn/courses/30/lessons/12921
10 4
5 3
'''
import math


def solution(n):
    arr = [True]*(n+1)
    cnt=0
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]==True:
            for j in range(2*i,n+1,i):
                arr[j]=False


    # cnt=arr.count(True)-2
    for i in range(len(arr)):
        if arr[i]==True:
            cnt+=1;
    return cnt-2

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.05ms, 10.1MB)
# 테스트 6 〉	통과 (0.70ms, 10.2MB)
# 테스트 7 〉	통과 (0.18ms, 10.4MB)
# 테스트 8 〉	통과 (0.47ms, 10.2MB)
# 테스트 9 〉	통과 (0.84ms, 10.2MB)
# 테스트 10 〉	통과 (26.03ms, 12.1MB)
# 테스트 11 〉	통과 (97.97ms, 16.8MB)
# 테스트 12 〉	통과 (30.31ms, 12.5MB)
# 효율성  테스트
# 테스트 1 〉	통과 (94.68ms, 16.9MB)
# 테스트 2 〉	통과 (90.92ms, 16.4MB)
# 테스트 3 〉	통과 (99.63ms, 16.9MB)
# 테스트 4 〉	통과 (91.87ms, 16.9MB)

# import math
#
# def solution(n):
#     arr = [True]*(n+1)
#     cnt=0
#     for i in range(2,int(math.sqrt(n))+1):
#         if arr[i]==True:
#             j=2
#             while i * j <= n:
#                 arr[i * j] = False
#                 j += 1
#     cnt=arr.count(True)-2
#     return cnt
# n=int(input())
# print(solution(n))


#정확성
# 테스트 1 〉	통과 (0.00ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.16ms, 10MB)
# 테스트 5 〉	통과 (0.10ms, 10.1MB)
# 테스트 6 〉	통과 (1.79ms, 10.2MB)
# 테스트 7 〉	통과 (0.44ms, 10.3MB)
# 테스트 8 〉	통과 (1.12ms, 10.1MB)
# 테스트 9 〉	통과 (1.98ms, 10.3MB)
# 테스트 10 〉	통과 (75.09ms, 12MB)
# 테스트 11 〉	통과 (222.18ms, 16.8MB)
# 테스트 12 〉	통과 (78.85ms, 12.3MB)

#효율성
# 테스트 1 〉	통과 (231.87ms, 16.9MB)
# 테스트 2 〉	통과 (220.37ms, 16.9MB)
# 테스트 3 〉	통과 (230.90ms, 17MB)
# 테스트 4 〉	통과 (239.83ms, 16.9MB)
