def solution(nums):
    answer = 0
    table = [nums[0]]
    for i in nums :
        if i not in table :
            table.append(i)
    if len(table) > int(len(nums) / 2) :
        answer = int(len(nums) / 2)
    else :
        answer = len(table)
    return answer