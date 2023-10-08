def solution(num_list):
    sums = sum(num_list)**2
    muls = 1
    for num in num_list : 
        muls *= num
    return 1 if sums>muls else 0