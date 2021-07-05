# 다시 풀면서 개선시킨 코드
def solution(p):
    if match(p): # 이미 '올바른 괄호 문자열'이라면 그대로 return
        return p
    else:
        return divide(p)

def divide(p): # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    if p == '' : # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        return p
    u, v = balance(p)
    if match(u): # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
            return u + divide(v) # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
        answer = '('+divide(v)+')' # 4-1, 4-2, 4-3
        for i in u[1:-1]: # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer #  4-5. 생성된 문자열을 반환합니다.

def balance(p): # '균형잡힌 괄호 문자열'인지 탐색
    count1 = count2 = 0
    for i, v in enumerate(p): # enumerate 사용하여 idx 변수 줄임
        if v == '(':
            count1+=1
        else :
            count2+=1
        if count1 == count2: # u는 '균형잡힌 괄호 문자열'로 더 이상 분리할 수 없어야하므로, 가장 작은 단위로 균형잡힌 괄호 문자열일 때 분리 시행 
            return p[:i+1], p[i+1:]
            
def match(p): # '올바른 괄호 문자열'인지 탐색, stack 이용
    stack = []
    for i in p :
        if i == '(' :
            stack.append(i)
        else :
            if stack :
                stack.pop()
            else :
                return False
    if stack :
        return False
    return True