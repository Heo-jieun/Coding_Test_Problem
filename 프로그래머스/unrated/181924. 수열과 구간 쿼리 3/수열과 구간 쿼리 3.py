def solution(arr, queries):
    for i in queries:
        pre = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = pre
    return arr