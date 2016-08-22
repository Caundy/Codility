def solution(A):
    A.sort()
    flag = 1
    for i in range(0, len(A)-1):
        if A[i]-1 != i:
            flag = 0
            break
    return flag



tablica = [1,3,39,5,6,2]

solution(tablica)

#wyrzuca na 1,2 elementowych