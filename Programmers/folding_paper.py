def solution(n):
    answer = [0]
    for i in range(1,n):
        # 그 전의 것 + 0 + 뒤집은 것 
        temp = convert(answer[::-1])  # 뒤집고 0,1 변환
        answer.append(0)
        answer += temp
    return answer

def convert(answer):
    temp = []
    for a in answer :
        if a == 0:
            temp.append(1)
        else:
            temp.append(0)
    return temp