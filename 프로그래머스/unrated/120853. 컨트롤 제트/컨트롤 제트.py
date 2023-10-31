def solution(s):
    nums = s.split(" ")
    print(nums)
    sums = 0
    for i in range(len(nums)):

        if nums[i] == 'Z':
            sums -= int(nums[i-1])
            
        else: 
            sums += int(nums[i])

        print(sums)
    return sums