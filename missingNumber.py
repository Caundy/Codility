def solution(A):
    A.sort()
    for i in range(0, len(A)):
        if (i<len(A)-1) and (A[i+1]-A[i] == 2):
            return (A[i+1] - 1)
        elif (i == len(A) - 1) and (A[-1] == i+2):
            return 1
        elif (i == len(A) - 1) and (A[-1] != i + 2):
            return A[-1]+1





tablica = [2,3,4,5,6,1,7]

solution(tablica)