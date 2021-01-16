# 백준 10828 스택 (신지원)

import sys

N = int(input()) #명령의 수 입력 받음
st = [] #스택으로 이용할 리스트
for i in range(N):
    com = sys.stdin.readline().rstrip().split() #수행시간을 줄이기 위해 사용된다고 한다
    if com[0] == "push": #push라면
        st.append(com[1]) #함께 입력받은 수를 push함
    elif com[0] == "pop": #pop이라면
        if not st: #리스트가 비었다면 -1을 출력
            print(-1)
        else: #있다면 맨 뒤에거 pop하고 출력
            print(st.pop())
    elif com[0] == "size": #스택의 크기
        print(len(st)) #리스트의 길이로 출력
    elif com[0] == "empty":
        if not st: #비어있다면
            print(1) #1 출력
        else: #아니라면 
            print(0) #0 출력
    elif com[0] == "top": #가장 마지막에 들어간 요소 출력
        if not st: #비어있다면 -1 출력
            print(-1)
        else: #아니라면 가장 마지막 요소 출력
            print(st[-1])