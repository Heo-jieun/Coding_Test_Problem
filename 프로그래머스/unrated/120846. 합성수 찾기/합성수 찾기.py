def solution(n):
    cnt = 0 
    for num in range(4, n+1) : 
        x = len([i for i in range(1, num+1) if num%i == 0 ])
        if x>= 3 : 
            cnt += 1
    return cnt