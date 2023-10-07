def solution(slice, n):
    count = 1
    while 1 :
        if slice*count >= n :
            return count
        count += 1
    