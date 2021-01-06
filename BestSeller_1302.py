# 백준 1302 베스트셀러 신지원

N = int(input()) #오늘 하루 팔린 책의 개수

dic = {} #책의 개수를 저장할 딕셔너리
max_count = 0 #제일 많이 팔린 책의 수
for i in range(N):
    name = input()
    if name in dic.keys(): #입력된 책이 이미 목록에 있다면
        count = dic[name] #원래 count 값을 추출하고
        count +=1 #1을 더한다
    else: #없다면 
        count = 1 #count는 1로 설정한다
    if count > max_count: #새로운 count값이 현재의 최고보다 높다면
        max_count = count #max_count를 업데이트한다
    dic[name] = count #딕셔너리를 count로 업데이트

dic_list = list(dic) #책의 이름만 리스트로 추출
max_books = [] #가장 많이 팔린 책들을 저장할 리스트
for i in range(len(dic_list)): 
    if max_count == dic[dic_list[i]]: #책이 최대만큼 팔렸다면 
        max_books.append(dic_list[i]) #리스트에 추가
max_books.sort() #사전순으로 정렬
print(max_books[0]) #가장 앞에 있는 책 출력