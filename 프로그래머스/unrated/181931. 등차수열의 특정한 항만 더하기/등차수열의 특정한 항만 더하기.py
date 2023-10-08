def solution(a, d, included):
    arr = [a]
    for i in range(1,len(included)) : 
        arr.append( arr[i-1] + d )
        
    answer = 0
    for i in range(len(included)):
            if included[i] : 
                answer += arr[i]
    return answer