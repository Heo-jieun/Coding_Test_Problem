def solution(s1, s2):
    cnt = 0 
    for s in s1:
        for c in s2:
            if s == c: 
                cnt += 1
    return cnt