# 백준 9935 문자열 폭발 (신지원)

text = input() #문자열을 입력받음
explode = input() #폭발 문자열을 입력받음

stack = [] #스택을 이용
for i in range(len(text)):
    stack.append(text[i]) #스택에 한 문자씩 넣은 후
    if text[i] == explode[-1]: #만약 이 문자가 폭발 문자열의 마지막 문자라면
        if "".join(stack[-len(explode):]) == explode: #이 앞의 문자열이 폭발 문자열과 일치한다면
            del stack[-len(explode):] #스택에서 폭발문자열 문자들을 모두 삭제한다
# 위 과정을 모두 반복한 뒤
if len(stack) == 0: print("FRULA") #아무것도 남아있지 않다면 FRULA를 출력
else: print("".join(stack)) #남아있다면 스택에 있는 문자들을 연결하여 출력