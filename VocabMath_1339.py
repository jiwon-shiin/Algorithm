# 백준 1339 단어 수학 (신지원)

N = int(input()) #단어의 개수
words = [] #단어들을 저장할 배열
for i in range(N):
    words.append(input())

important = {} #중요도를 저장할 딕셔너리(클수록 높은 수 배정할 것)
#중요도 예시) GCF와 ACDEB라면 A의 중요도는 10000, C의 중요도는 1010
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in important.keys(): #이미 추가한 알파벳이라면
            important[words[i][j]] = important[words[i][j]]+10**(len(words[i])-1-j) #원래 값에 더해줌
        else: #처음 나오는 알파벳이라면
            important[words[i][j]] = 10**(len(words[i])-1-j) #딕셔너리에 중요도 값 저장

important = list(important.items()) #(알파벳, 중요도) 튜플 형태의 리스트로 변환하여
important.sort(key = lambda x:-x[1]) #중요도에 따라 정렬한다
nums = {} #알파벳에 대응하는 숫자를 저장할 딕셔너리
num = 9 #가장 큰 수 부터 적용
for i in range(len(important)):
    nums[important[i][0]] = num #알파벳 별로 숫자 부여
    num -= 1

final = [] #최종 완성되는 수들을 저장할 리스트
for i in range(len(words)):
    word_to_num = "" #각 단어들을 숫자로 바꾸는데 이용할 문자열
    for j in range(len(words[i])):
        word_to_num += str(nums[words[i][j]]) #문자열 형태로 순서대로 나열하고
    final.append(int(word_to_num)) #정수형으로 바꾸어 최종 숫자를 저장
    
print(sum(final)) #최종 숫자들의 합을 출력
