"""
카운터에서는 거스름돈으로 사용할 500,100,50,10원의 동전이 무한히 존재한다.
손님에게 거슬러 줘야하는 돈이 N원일 때, 거슬러 줘야 할 동전의 최소개수를 구하라.
단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.
"""

N = int(input())

coins = [500,100,50,10]
count = 0

for coin in coins:
    count += N // coin
    N %= coin

print(count)