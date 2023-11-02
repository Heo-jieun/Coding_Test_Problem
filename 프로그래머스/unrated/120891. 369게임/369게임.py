def solution(order):
    game = ['3','6','9']
    sum = 0
    for num in game : 
        sum += str(order).count(num)
    return sum