# 백준 2839

def sugar(kilo):
    n = kilo//5 #5kg의 개수를 최대로 했을 때
    if (kilo - n*5)%3 == 0: #3kg 하나 또는 0개로 N이 완성되는 경우
        return n + (kilo - n*5)//3 
    else:
        rem = kilo % 5
        temp = kilo - rem
        while (temp != 0): #5의 배수로 줄여가며 5kg 봉지를 최대로 유지하며
            if (kilo-temp) % 3 == 0: #3의 배수와의 합으로 N이 완성되는 경우
                return temp//5 + (kilo-temp)//3
            temp -= 5
        if kilo % 3 == 0: #5kg짜리 없이 3kg 만으로 N이 완성되는 경우
            return kilo // 3
    return -1 #5kg와 3kg로 N을 완성할 수 없다면

N = int(input())
print(sugar(N))