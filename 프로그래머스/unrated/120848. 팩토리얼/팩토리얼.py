def solution(n):
    fact = 1
    i = 1
    while 1 : 
        fact *= i
        if fact >= n : 
            answer = i
            break
        i += 1
    if fact > n : 
        answer -= 1
    return answer