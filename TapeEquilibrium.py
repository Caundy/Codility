def solution(A):
    differences = []
    if len(A)!=0:
        for x in A:
            if (int(x) > 0) and (int(x) < len(A)):
                first_half = sum(A[0:(int(x))])
                second_half = sum(A[int(x):])
                differences.append(abs(first_half-second_half))
        return min(differences)


lista = [1,2,3,4,5,6,7,8,9]
solution(lista)

#DO POPRAWY, za dlugo chodzi, zle wyniki