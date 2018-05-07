m, n = 5, 3
lis = [0] * m
for j in range(n):
  a, b, k = map(int, input().split())
  for i in range(a-1, b):
    lis[i] += k
print(max(lis))