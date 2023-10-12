def solution(n, control):
    controls = {"w" : 1 , "s" : -1 , "d" : 10,  "a" : -10}
    for str in control :
        n += controls[str]
    return  n