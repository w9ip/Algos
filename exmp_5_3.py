# Манхэттенское расстояние.

x1, y1 = input().split()
x2, y2 = input().split()

dx = abs(int(x1) - int(x2))
dy = abs(int(y1) - int(y2))

print(dx + dy)
