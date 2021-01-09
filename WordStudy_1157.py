# 백준 1157 단어공부 (신지원)

text= input().upper() #입력받은 문자열을 대문자로 저장.

dic = {} #개수를 관리할 딕셔너리 생성
for i in range(len(text)):
    if text[i] in dic.keys(): #이미 딕셔너리에 있는 문자라면
        dic[text[i]] += 1 #1을 더하고
    else: #없다면
        dic[text[i]] = 1 #개수를 1로 하여 딕셔너리에 추가한다

max_counts=[] #최다 사용 문자들을 저장할 리스트
max_count = max(dic.values()) #가장 많이 사용된 알파벳은 몇개인지
for key, value in dic.items(): #딕셔너리의 요소들 중
    if value == max_count: #value가 최댓값이라면
        max_counts.append(key) #리스트에 추가한다
        
if len(max_counts)>1: print("?") #가장 많이 사용된 문자가 2개 이상이라면 ?를 출력
else: print(max_counts[0]) #아니라면 그 문자를 출력