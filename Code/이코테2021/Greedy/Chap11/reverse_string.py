S = input()
target = '0' if S.count('0') < S.count('1') else '1'

count = 0
is_target = False
for num in S:
    if num == target:
        is_target = True
    else:
        if is_target:
            count += 1
        is_target = False

print(count)