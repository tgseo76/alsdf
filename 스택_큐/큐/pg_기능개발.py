'''
https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
1 1 50
100 2 1

95 90 99 99 80 99
1 1 1 1 1 1
'''
progresses = list(map(int,input().split()))
speeds=list(map(int,input().split()))
answer=[]
new_arr = []
for _ in range(len(speeds)):
    new_arr.append(speeds[_])

while(len(progresses)>0):
    cnt=0
    if(len(progresses)!=0):
        while ((progresses[0]+speeds[0])>=100):
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
            new_arr.pop(0)
            if (len(progresses) == 0):
                break
        for k in range(len(speeds)):
            speeds[k]=new_arr[k]+speeds[k]
        if cnt>0:
            answer.append(cnt)

print(answer)

# def solution(progresses, speeds):
#     answer=[]
#     i = 1
#     new_arr = []
#     for _ in range(len(speeds)):
#         new_arr.append(speeds[_])
#
#     while(len(progresses)>0):
#
#         i+1
#         cnt=0
#         if(len(progresses)!=0):
#             while ((progresses[0]+speeds[0])>=100):
#                 cnt+=1
#                 progresses.pop(0)
#                 speeds.pop(0)
#                 new_arr.pop(0)
#                 if (len(progresses) == 0):
#                     break
#             for k in range(len(speeds)):
#                 speeds[k]=new_arr[k]+speeds[k]
#             if cnt>0:
#                 answer.append(cnt)
#
#     return answer