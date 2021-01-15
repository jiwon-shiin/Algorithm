#백준 5585 거스름돈 (신지원)

def money(pay):
    pay = 1000-pay
    money = [500,100,50,10,5,1]
    total = 0
    for i in money:
        if pay//i:
            total += pay//i
            pay %= i
    return total

mon = int(input())
print(money(mon))