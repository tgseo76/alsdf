'''https://codeup.kr/problem.php?id=2083

n개로 이루어진 정수 집합에서 원하는 수의 위치를 찾으시오.

단, 입력되는 집합은 오름차순으로 정렬되어 있으며, 같은 수는 없다.

3 7
2 5 7

3
'''

n,s=list(map(int, input().split( ))) #정수 n & 찾고자 하는 값 s
arr=list(map(int, input().split( ))) # n개의 정수

if s in arr:
    print(arr.index(s)+1)
else:print(-1)


