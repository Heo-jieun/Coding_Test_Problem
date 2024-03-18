def solution(num_list):
    mul = 1
    if len(num_list)<11 :
        for i in num_list:
            mul=mul*i
        answer = mul
    else :
        answer = sum(num_list)
    return answer