# 백준 15904 UCPC는 무엇의 약자일까? (신지원)

text = input() #문자열이 주어짐
UCPC = True #적절히 축약해 UCPC로 만들 수 있는지 여부
for i in "UCPC": #UCPC를 각각
    index = text.find(i) #문자열에서 인덱스를 찾고 (왼쪽부터)
    if index == -1: #find 함수는 존재하지 않는 경우 -1을 반환하므로
        UCPC = False #존재하지 않는다는 의미에서 False로 바꾼 후
        break #반복문 종료
    text = text[index:] #주어진 텍스트를 찾은 인덱스부터로 split하여 뒷 부분에서 찾도록.
if UCPC: #모두 찾아서 UCPC가 True로 유지된 경우
    print("I love UCPC") #축약 가능하므로 I love UCPC 출력
else: #False인 경우
    print("I hate UCPC") #UCPC를 만들 수 없는 것이므로 I hate UCPC 출력
