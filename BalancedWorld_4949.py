# 백준 4949 균형잡힌 세상 (신지원)

while True:
    text= input() #문자열을 입력받고
    if text == ".": #종료의 의미인 .이라면 반복문 종료
        break
    answer = "yes" #정답을 저장할 변수인데 항상 yes로 초기화
    stack = [] #스택으로 쓸 리스트 초기화
    for i in range(len(text)): #입력받은 문자열에 대해
        if text[i] == "[" or text[i] == "(": #[또는 (라면
            stack.append(text[i]) #스택에 추가하고
        elif text[i] == "]" or text[i] == ")": #]또는 )라면
            if not stack: #스택이 비어있다면
                answer = "no" #정답을 no로 바꾼 후 종료
                break
            tmp = stack.pop() #스택에서 pop하여
            if not ((tmp,text[i]) == ("(",")") or (tmp,text[i]) == ("[","]")): #괄호쌍이 맞는지 비교한 후 틀리다면
                answer = "no" #정답을 no로 바꾸고
                stack.append(tmp) #스택에 다시 tmp를 push 한 후
                break #종료
        if i == len(text)-1 and stack: #마지막까지 돌았는데 스택에 아직 괄호가 남아있다면 짝이 맞지 않는 것이므로
            answer= "no" #정답을 no로 바꿈
    print(answer) #정답을 no로 바꾼 경우에는 no가 출력, 아닌 경우에는 yes가 출력됨