'''
https://school.programmers.co.kr/learn/courses/30/lessons/42883


"1924"
2

"94"
---
"4177252841"
4

"775841"
'''
def solution(number, k):
    number = list(number)
    dap = [number.pop(0)]

    for i in number:
        if dap[-1] < i:
            while dap and dap[-1] < i and k > 0:
                dap.pop()
                k -= 1
            dap.append(i)
        elif k == 0 or dap[-1] >= i:
            dap.append(i)

    if k:
        dap = dap[:-k]
    answer=''.join(dap)

#
# number="1924"
# k=2
#
# number=list(number)
# dap=[number.pop(0)]
#
# for i in number:
#     if dap[-1] < i:
#         while dap and dap[-1] < i and k>0:
#             dap.pop()
#             k-=1
#         dap.append(i)
#     elif k==0 or dap[-1] >= i:
#         dap.append(i)
#
# if k:
#     dap=dap[:-k]
# aaa=''.join(dap)
#
# print(aaa)

