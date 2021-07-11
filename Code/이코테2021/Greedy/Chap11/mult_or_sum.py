S = input()
result = int(S[0])
for s in S[1:]:
    num = int(s)
    result = result + num if result == 0 or num == 0 else result * num

print(result)