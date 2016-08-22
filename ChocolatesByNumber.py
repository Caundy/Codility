from fractions import gcd

def solution(N, M):
    empty_wrapper = False
    count = 1
    chocolates = [] #all chocolates to be eaten
    chocolates.insert(0, 0)  #we start by eating the first one ([0])
    current = 0
    while(empty_wrapper!=True):
        current = (current + M) % N #current position
        if current in chocolates: #eaten
            empty_wrapper = True
        else:                       #not eaten
            chocolates.append(current)
            count += 1
    return count


#solution(947853, 4453)

# do przerobienia pod wzgledem efektywnosci czasowej (wyniki ok)
# najwiekszy wspolny dzielnik, najmniejsza wspolna wielokrotnosc

LCM = 947853 * 4453 /  gcd(947853, 4453)
print LCM/947853