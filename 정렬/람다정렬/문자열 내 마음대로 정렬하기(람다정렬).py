def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer

strings=["abce", "abcd", "cdx"]
n=2
answer=[]
answer=sorted(strings,key=lambda x:(x[n]))

print(solution(strings,n))
print(answer)