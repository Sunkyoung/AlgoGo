def solution(answers):
    answer = []
    score1 = score2 = score3 = 0
    ans1 = [1,2,3,4,5] # 1번 수포자가 찍는 방식
    ans2 = [2,1,2,3,2,4,2,5] # 2번 수포자가 찍는 방식
    ans3 = [3,3,1,1,2,2,4,4,5,5] # 3번 수포자가 찍는 방식
    for i,v in enumerate(answers): 
        # 반복되니까 길이의 나머지로 방식의 찍은 답을 인덱스로 활용
        if v == ans1[i%len(ans1)] :
            score1 += 1
        if v == ans2[i%len(ans2)] :
            score2 += 1
        if v == ans3[i%len(ans3)]:
            score3 += 1
    m = max(score1,score2,score3) # 가장 많은 문제 맞힌 갯수
    # score를 배열로 했다면 이부분 코드를 더 줄일 수 있을 것
    if score1 == m: # 하나씩 최고로 많이 문제 맞혔는지 비교
        answer.append(1)
    if score2 == m:
        answer.append(2)
    if score3 == m:
        answer.append(3)
    return answer