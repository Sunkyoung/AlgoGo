#카카오 코테 당시 작성 코드
def solution(p):
    if findmatch(p):
        return p
    else:
        return divide(p)

def divide(p): # u, v로 분리
    cnt_l=0
    cnt_r=0
    idx = 0
    u = ''
    v = ''
    for a in p:
        if a=='(':
            cnt_l += 1
        else :
            cnt_r += 1
        idx += 1
        if cnt_l == cnt_r:
            u += p[:idx]
            v += p[idx:]
            break
    
    if findmatch(u) :
        if v :
            return u + divide(v)
        else :
            return u
    else :
        answer = '('+divide(v)+')'
        if u :
            u = u[1:len(u)-1]
            for a in u:
                if a == '(' :
                    answer += ')'
                else :
                    answer += '('
        return answer
                
def findmatch(p): #올바른 문자열
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(i)
        elif p[i] == ')':
            if stack :
                stack.pop()
            else :
                return False
    return True