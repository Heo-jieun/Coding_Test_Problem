def solution(my_string):
    oi = ['a', 'e', 'i', 'o', 'u']
    for s in oi : 
        my_string = my_string.replace(s, "")

    return my_string