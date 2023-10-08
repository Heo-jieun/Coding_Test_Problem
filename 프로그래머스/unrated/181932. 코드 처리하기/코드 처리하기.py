def solution(code):
    ret = ""
    mode = 0
    for i in range(len(code)) : 
        if code[i] == '1':
            if mode == 1:
                mode = 0
            else :
                mode = 1
        elif mode == 1:
            if i%2 != 0 :
                ret += code[i]
        else : 
            if i%2 == 0 :
                ret += code[i]
    return "EMPTY" if len(ret) == 0 else ret