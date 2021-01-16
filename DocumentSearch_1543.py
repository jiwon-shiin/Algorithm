# 백준 1543 문서 검색 (신지원)

text = input() #문서가 입력됨
find = input() #검색하고 싶은 단어가 입력됨
index = 0 #인덱스
count = 0 #개수
while True:
    index = text.find(find) #문서에서 단어의 인덱스를 찾음
    text = text[index+len(find):] #인덱스와 단어의 길이만큼 자르고 그 뒤에서 다시 검색하도록
    if index == -1: #존재하지 않는다면 -1을 반환하기 때문에 -1이면
        break #종료
    count += 1 #그렇지 않다면 개수 +1
print(count) #총 개수 출력