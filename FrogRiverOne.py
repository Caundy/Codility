def solution(X, A):
    #deklaracja tablicy pomocnicznej
    if max(A) > len(A):
        help_array = [0] * (max(A)+1)
    else:
        help_array = [0] * (len(A)+1)
    print help_array[1]
    #deklaracja zmiennych do petli while
    i = 0
    licznik = 0
    przeskoczyla = 2
    babol = 0

    while (help_array[1:X+1] != 1):
        help_array[A[i]] = int(1)
        if A[i] <= X:
            licznik += 1
        print help_array
        if i <= len(A)-2:
            i += 1
        elif i == len(A)-1: #przejscie do ostatniego indeksu
            for x in range(1, X + 1):
                if (help_array[x] == 1):
                    przeskoczyla = 1
                else:
                    babol = 1
            break
    if babol == 0:
        print licznik
    else:
        return -1



tablica = [1,2,3,4,8,5,7,8]
dystans = 5
solution(dystans, tablica)
