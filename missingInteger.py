def solution(A):
    A.sort()
    if max(A)>len(A):
        help_array = [0] * max(A)
    else:
        help_array = [0] * len(A)
    help_array.insert(0, 1) #dla wygody, wtedy indeks z wartoscia 0 to liczba, ktorej brakuje
    if len(A) == 1 and A[0] < 0:
        return 1
    elif len(A) == 1 and A[0] >= 0:
        return A[0]+1
    for x in range(0, len(A)):
        if A[x] >= 0:
            help_array[A[x]] = 1
    for i in range(0, len(help_array)):
        if help_array[i]!= 1:
            return i



tablica = [1,2,3,2,4,6]

solution(tablica)