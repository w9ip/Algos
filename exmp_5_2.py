# Нахождение n-того числа Фибоначчи.

# Мой вариант:
n = int(input())
F0, F1 = 0, 1
i = 3
while i <= n:
  F0, F1 = F1, F0 + F1
  i += 1
print(0 if n == 0 else F0 + F1)

# Вариант приведенный в книге:
n = int(input())
f = [0, 1]
while len(f) <= n:
  f.append(f[-1] + f[-2])
print(f[n])
