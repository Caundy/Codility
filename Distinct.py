from collections import Counter

def solution(A):
    return len(Counter(A).most_common())



tablica = [2,1,3,2,1]
solution(tablica)