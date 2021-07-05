result = set()

def solution(N, number):
    for i in range(8):
        op1 = str(N)*i
        for j in range(i):
            if i+j+1 < 8 :
                op2 = str(N)*(j+1)
                temp = list(result)
                print(op1, op2)
                for t in temp: # 기존에 있는 계산 값과 연산
                    calculate(t,int(op2))
                calculate(int(op1),int(op2))
                if number in result :
                    return i+j+1
    return -1
    
def calculate(op1, op2):
    result.add(op1 + op2)
    result.add(op1 - op2)
    result.add(op1 * op2)
    if op2 != 0 :
        result.add(op1 // op2)

print(solution(5, 31168))