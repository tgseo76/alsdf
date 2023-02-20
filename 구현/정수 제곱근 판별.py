'''
https://school.programmers.co.kr/learn/courses/30/lessons/12934

'''
import math

def solution(n):
    n = math.sqrt(n)
    if (n == (int(n))):
        return(math.pow(n + 1, 2))
    else:
        return(-1)


def solution2(n):
    n = n**0.5
    if (n == (int(n))):
        return(int((n+1)**2))
    else:
        return(-1)