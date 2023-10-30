def solution(my_string):
    nums =[]
    for s in my_string : 
        if 47 < ord(s) < 58 : 
            nums.append(int(s))
    nums.sort()
    return nums