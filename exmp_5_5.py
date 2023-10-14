# Проверка перестановки.

# Вариант из книги:
# ...

# Мой вариант:
nums = tuple(map(int, input().split()))

if len(nums) == max(nums) and (2 not in (nums.count(e) for e in nums)):
  print('OK')
else:
  print('BAD')
