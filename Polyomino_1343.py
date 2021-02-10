# 백준 1343 폴리오미노 (신지원)

import sys
board = sys.stdin.readline().rstrip("\n") #보드판 입력받음

poly = "" #정답을 저장할 변수
count = 0 #연속된 X의 개수를 셀 변수. (최대 2까지만 카운트 할 것임)
for i in board: #보드판을 돌면서
    if i == "X": #X라면
        count += 1 #카운트 증가시키고
        if count == 2: #카운트가 2라면
            poly += "BB" #BB 폴리오미노를 놓고
            count = 0 #카운트 초기화
    elif i == ".": #.일 때 (카운트는 0또는 1일 것임)
        if count == 1: #카운트가 1이라면 모두 덮는것이 불가능한 상황이므로
            break #반복문 종료
        poly += "." #정답에는 . 추가
if count == 1: #카운트가 1인 경우 -> 모두 덮는 것이 불가능. (덮다가 실패하는 경우, 애초에 하나인 경우 등 모두 포함)
    poly = "-1" #정답을 구할 수 없으므로 -1

poly = poly.replace("BBBB","AAAA") #연속한 B 4개가 있다면 A 4개로 바꿀 수 있음. 사전순이므로 왼쪽부터
print(poly) #정답 출력