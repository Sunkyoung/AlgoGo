S = input()
result = int(S[0])
for s in S[1:]:
    num = int(s)    
    if result == 0 or num == 0:
        result += num
    else:
        result *= num

print(result)