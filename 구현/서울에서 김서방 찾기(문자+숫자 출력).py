'''
https://school.programmers.co.kr/learn/courses/30/lessons/12919
'''

def solution(seoul):
    cnt = seoul.index("Kim")
    return "김서방은 {}에 있다".format(cnt)


seoul=["Jane", "Kim"]
print(solution(seoul))