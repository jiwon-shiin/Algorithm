# 백준 4344 평균은 넘겠지 (신지원)

def percent():
    a = list(map(int,input().split())) #n명과 n명의 점수
    n = a[0] #n 추출
    score = a[1:] #점수 리스트
    add = sum(score) #전체 합
    mean = add/n #평균
    student = 0 #평균을 넘는 학생 수 구할 것
    for i in range(n):
        if score[i]>mean:
            student += 1 #평균 넘으면 1 추가
    per = (student/n)*100 #퍼센트 구하기 
    print("{0:.3f}%".format(per)) #소수점 셋째 자리까지 출력

C = int(input()) #테스트 케이스 수
for i in range(C):
    percent() #퍼센트 구하기