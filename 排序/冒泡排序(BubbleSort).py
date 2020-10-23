from randomList import randomList

for num in range(1,20):
    nums = randomList.randomList(20)

    # 不优化
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print(f'第{nums}次结果为',nums)

    # 优化
    for i in range(len(nums)-1):
        flag = True
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = False
        if flag:
            break
    print(f'第{nums}次结果为',nums)