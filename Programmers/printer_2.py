def solution(priorities, location):
    answer = 1
    m = max(priorities)
    while True:
        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        temp = priorities.pop(0)
        # 3. 그렇지 않으면 J를 인쇄합니다. 
        if temp == m :
            if location == 0: # 내가 인쇄 요청한 문서가 출력할 차례
                return answer
            answer += 1 # 요청하지 않은 문서 인쇄되므로 +1
            location -= 1
            m = max(priorities) # 최대값 재설정
        else: # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
            priorities.append(temp)
            if location == 0: # 대기 목록의 가장 마지막에 넣으므로 0일때 이와같이 처리
                location = len(priorities) - 1
            else:
                location -= 1