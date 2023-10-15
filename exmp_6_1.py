# Пара с минимальным произведением

# Дан массив чисел, выбрать 2 числа - произведение которых минимально.

# Мой вариант:
# n = int(input())
# nums = list(map(int, input().split()))
nums = [2, 5, 3, -1, 7, 9, 0]

min1, min2 = nums[0], nums[1]
if min1 > min2:
  min1, min2 = min2, min1
  
for i in range(2, len(nums)):
  if nums[i] < min1:
    min2, min1 = min1, nums[i]

print(min1, min2)