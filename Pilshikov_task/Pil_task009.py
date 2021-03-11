#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Task 3.19 page 18
condition for the existence of a triangle

"""

# x, y, z - side of a triangle
x, y, z = int(input("input side x: ")), int(input("input side y: ")), int(input("input side z: "))
print('Yes' if (x < y + z) and (y < x + z) and (z < x + y) else 'No')
