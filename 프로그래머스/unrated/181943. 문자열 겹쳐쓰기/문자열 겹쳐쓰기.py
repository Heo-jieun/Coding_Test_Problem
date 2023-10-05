def solution(my_string, overwrite_string, s):
    last_idx = len(overwrite_string) + s
    answer = my_string[:s] + overwrite_string + my_string[last_idx:]
    return answer