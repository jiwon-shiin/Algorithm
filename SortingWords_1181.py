# 백준 1181 단어 정렬 (신지원)

N = int(input()) #단어의 개수 입력받고

words=[]
for i in range(N):
    words.append(input()) #단어를 입력받고 words 리스트에 넣는다

words = list(set(words)) #중복 단어 제거
words = sorted(words,key = lambda x:(len(x),x)) #길이가 짧은 순, 길이가 같으면 사전 순으로 정렬
for i in words:
    print(i)