S = input()

digits, alpha = [], []
for s in S:
    if s.isdigit():
        digits.append(int(s))
    else:
        alpha.append(s)

alpha.sort()
digits.sort()

result = ''.join(alpha) + str(sum(digits))
print(result)