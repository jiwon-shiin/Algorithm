# 백준 9012

def isVPS(text):
    stack = []
    for i in range(len(text)):
        if text[i] == "(":
            stack.append(text[i])
        if text[i] == ")":
            if len(stack) == 0: 
                print("NO")
                return
            stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

T = int(input())
for i in range(T):
    text = input()
    isVPS(text)