N = int(input())

score = str(N)
left_score, right_score = 0, 0
for i, num in enumerate(score):
    if i < int(len(score)/2):
        left_score += int(num)
    else:
        right_score += int(num)

result = 'LUCKY' if left_score == right_score else 'READY'
print(result)