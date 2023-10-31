def solution(array, height):
    answer = 0 
    for he in array :
         if he > height : 
                answer += 1
    return answer