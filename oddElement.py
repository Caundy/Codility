from collections import Counter

def solution(A):
    if len(A) != 0:
        least_common = Counter(A).most_common()[-1][0]
        return least_common

A = [1,22,3,3,4,5]

solution(A)