N = int(input())
coins = list(map(int, input().split()))

result = 1
coins.sort()

for coin in coins:
    if result < coin:
        break
    result += coin

print(result)