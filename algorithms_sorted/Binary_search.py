#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)


def LowerBound(nums, key):
    left = -1
    right = len(nums)

    while right > left + 1:
        middle = (left + right) // 2
        if nums[middle] >= key:
            right = middle
        else:
            left = middle
    return right





