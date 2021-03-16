#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)


def bubble_sort(nums):
    last_item = len(nums) - 1

    for z in range(0, last_item):
        for x in range(0, last_item):
            if nums[x] > nums[x + 1]:
                nums[x], nums[x + 1] = nums[x + 1], nums[x]
    return nums
