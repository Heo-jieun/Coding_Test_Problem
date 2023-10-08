def solution(num_list):
    hol = ''
    jac = ''
    for num in num_list : 
        if num % 2 == 0 :
            jac += str(num)
        else : 
            hol += str(num)
    return int(hol) + int(jac)