# 백준 7785 회사에 있는 사람 (신지원)

n= int(input()) #기록된 출입 기록의 수 n개 입력

enter = set() #출입한 사람들을 set 자료구조로 관리할 것이다.
for i in range(n):
    name, state = input().split() #이름과 
    if state == "enter": #enter했다면
        enter.add(name) #set에 추가하고
    else: #leave했다면
        enter.remove(name) #제거한다
atwork = list(enter) #정렬하기 위해 set을 리스트로 바꾸고
atwork.sort(reverse = True) #리스트를 내림차순으로 정렬한다

for i in range(len(atwork)): #남아있는 사람들의 목록을
    print(atwork[i]) #한 명씩 출력한다