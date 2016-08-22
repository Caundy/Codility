def solution(A, K):
    if len(A)!=0:
        for x in range(1, K+1):
            A.insert(0, A[-1])
            del A[-1]
        return A


