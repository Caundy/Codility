#iterations
def solution(N):
    binary = str(bin(N))[2:] #przechodzimy od drugiego miejsca ze wzgledu na format wypisania binary
    znaki = []
    for x in binary:
        znaki.append(x) #tablica cyfr 1, 0

    max_ciag, licznik, i = 0, 0, 0

    while(i < len(znaki)): #od indeksu 0 do ostatniego
        if znaki[i] == '0':
            licznik += 1 #zwieksz licznik, bo zero
        #jesli   i jest rozne od ostatniego i nastepny to 1  ALBO i jest ostatnie i jest rowne 0
        else:
            if licznik > max_ciag:
                max_ciag = licznik
            licznik = 0
        i += 1
    return max_ciag

solution(923983298)