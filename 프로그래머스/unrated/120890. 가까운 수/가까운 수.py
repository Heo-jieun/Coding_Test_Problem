def solution(array, n):
    answer = array[0]
    de = 100
    for num in array:
        if abs(n-num) < de:
            de = abs(n-num)
            answer = num 
        elif abs(n-num) == de:
            answer = answer if answer < num else num
            
    return answer