# 백준 2839

def sugar(kilo):
    rem = kilo % 5 #temp를 N이하 최대의 5의 배수로 만들어주기 위해
    temp = kilo - rem
    while (temp != 0): #temp가 0이 되기전까지 5씩 감소시키며 temp를 5의 배수로 유지
        if (kilo - temp) % 3 == 0: #5kg와 3kg의 조합으로 N이 완성되는 경우
            return temp//5 + (kilo-temp)//3 #각각의 개수를 반환
        temp -= 5
    if kilo % 3 == 0: #5kg짜리 없이 3kg 만으로 N이 완성되는 경우
        return kilo // 3
    return -1 #5kg와 3kg로 N을 완성할 수 없다면

N = int(input())
print(sugar(N))