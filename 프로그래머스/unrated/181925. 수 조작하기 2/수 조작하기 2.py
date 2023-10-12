def solution(numLog):
    n = 0
    answer = ""
    controls = { 1 : "w" , -1 : "s", 10 : "d", -10 : "a"}
    for i in range(len(numLog)-1) : 
        n = numLog[i+1] - numLog[i]
        if n in controls:
            answer += controls[n]
    return answer