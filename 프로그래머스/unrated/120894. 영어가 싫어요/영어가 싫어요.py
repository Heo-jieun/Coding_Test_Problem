def solution(numbers):
    alpha = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" :7, "eight" : 8, "nine" : 9 }
    for a in alpha:
        numbers = numbers.replace(a, str(alpha[a]))
    return int(numbers)