N, M = map(int, input().split())
K = list(map(int, input().split()))

count = 0
weight = K

for i, bowl in enumerate(K):
    count += len(weight) - weight.count(bowl)
    weight = K[i+1:]

print(count)