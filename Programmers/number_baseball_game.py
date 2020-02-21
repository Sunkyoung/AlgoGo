import itertools

def solution(baseball):
    answer = 0
    # 모든 경우의 수, all에 담음
    all = list(itertools.permutations(range(1,10),3)) # 1-9까지의 수 세 개의 수로 구성한 순열
    for a in all:
        flag = False
        for round in baseball:
            num = str(round[0])
            s, b = check(a, num) # 경우의 수와 질문한 숫자 간의 s, b 카운트 비교
            if s != round[1] or b != round[2] :
                flag = False
                break
            flag = True # 카운트가 같다면 flag를 true로 설정
        if flag is True: # input으로 주어진 케이스에 대해 모두 만족한다면 answer + 1
            answer += 1
    return answer

def check(a, num):
    s , b = 0 , 0 
    for i in range(3) :
        # strike가 되는 경우
        if str(a[i]) == num[i] :
            s += 1
            continue # continue 사용안하면 중복 볼 카운트 됨
        # ball이 되는 경우
        if str(a[i]) in num :
            b += 1
    return s, b