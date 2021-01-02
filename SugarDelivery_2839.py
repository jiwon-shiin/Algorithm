# 백준 2839

def sugar(kilo):
    n = kilo//5
    if (kilo - n*5)%3 == 0:
        return n + (kilo - n*5)//3
    else:
        rem = kilo % 5
        temp = kilo - rem
        while (temp != 0):
            if (kilo-temp) % 3 == 0:
                return temp//5 + (kilo-temp)//3
            temp -= 5
        if kilo % 3 == 0:
            return kilo // 3
    return -1

n = int(input())
print(sugar(n))