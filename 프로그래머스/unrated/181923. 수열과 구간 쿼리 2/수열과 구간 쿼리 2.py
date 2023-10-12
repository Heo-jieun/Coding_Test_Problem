def solution(arr, queries):
    answer = []
    
    for querie in queries:
        list = []
        for i in range(querie[0], querie[1]+1) :
            # print(i)
            if arr[i] > querie[2] :
                list.append(arr[i])
        # print()
        if len(list) != 0 : 
            answer.append(min(list))
        else : 
            answer.append(-1)
    return answer