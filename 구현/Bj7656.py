'''
https://www.acmicpc.net/problem/7656

Let me ask you two questions. What is the answer to life? What is life? What is the answer to the universe?


Forty-two is the answer to life.
Forty-two is the answer to the universe.
'''
#Test-case
# What is? What is? What is?
# What is? Let me ask you two questions. What is life? Let me ask you two questions. Let me ask you two questions. What is life?

a=list(map(str, input().split("What is")))
dap=[] # ['', ' life', ' life']
# print(a) #['', '? Let me ask you two questions. ', ' life? Let me ask you two questions. Let me ask you two questions. ', ' life?']
for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j]=="?"):
            dap.append(a[i][:j])
for i in range(len(dap)):
    print("Forty-two is"+dap[i]+".")






