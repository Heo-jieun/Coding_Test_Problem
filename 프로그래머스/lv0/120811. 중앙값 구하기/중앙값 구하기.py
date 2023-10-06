
def solution(array):
    array.sort()
    idx = int((len(array)-1) /2)
    return array[idx]