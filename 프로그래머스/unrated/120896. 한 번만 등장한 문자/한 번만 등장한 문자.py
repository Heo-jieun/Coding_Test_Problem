def solution(s):
    char_list = []
    for char in s: 
        if s.count(char) == 1:
            char_list.append(char)
    return "".join(sorted(char_list))