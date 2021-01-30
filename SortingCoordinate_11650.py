# 백준 11650 좌표 정렬하기 (신지원)

N = int(input()) #좌표의 수
dots = [] #좌표를 저장할 리스트
for i in range(N):
    x, y = map(int,input().split()) #정수형으로 x,y 좌표값을 입력받고
    dots.append((x,y)) #튜플형으로 리스트에 추가

dots.sort(key=lambda x:(x[0],x[1])) #x 오름차순, x좌표가 같다면 y오름차순으로 정렬
for i in dots:
    print(i[0],i[1]) #순차적으로 출력