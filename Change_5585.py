#백준 5585 거스름돈 (신지원)

def money(pay):
    pay = 1000-pay #1000엔에서 거스름돈을 계산할 것이기 때문에
    money = [500,100,50,10,5,1] #반복문을 통해 간결하게 하기 위해 화폐를 담아줌
    total = 0 #최종 거스름돈의 개수
    for i in money: 
        if pay//i: #몫이 존재한다면. 나누어질 수 있다면.
            total += pay//i #몫을 거스름돈의 개수에 추가.
            pay %= i #나머지를 다시 반복시켜 더 작은 단위로 거스름돈을 받을 수 있도록.
    return total

mon = int(input()) #구매한 가격
print(money(mon)) #거스름돈 개수 출력