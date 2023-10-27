def solution(numbers, k):
    idx = 0
    for i in range(k-1):
        idx += 2
        if idx >= len(numbers):
            idx -= len(numbers)
        num = numbers[idx]
    return num