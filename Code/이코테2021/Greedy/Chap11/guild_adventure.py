N = int(input())
degree_of_horror = list(map(int, input().split()))

count = 0
degree_of_horror.sort(reverse=True)

while True:
    max_value = degree_of_horror[0]
    if max_value >= len(degree_of_horror):
        if max_value == len(degree_of_horror):
            count += 1
        break
    degree_of_horror = degree_of_horror[max_value:]
    count += 1

print(count)