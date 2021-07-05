# java to python
import heapq
def solution(priorities, location):
    answer = 1
    heap = [] # 우선순위 반영한 인쇄 대기목록
    for i, v in enumerate(priorities): # 우선순위 큐에 넣기
        heapq.heappush(heap,-v) # 숫자가 클 수록 중요하기 때문에 음수로 넣기
    
    # 몇번째에 있는 지 탐색하는 과정
    while heap: # 인쇄 대기목록에 요소가 있을 동안 반복
        for i in range(len(priorities)) :
            if priorities[i] == -heap[0]: # 대기목록의 가장 앞의 값과 우선순위 배열 값이 같을 때
                if i == location: # 우선순위 배열에서 내가 찾고자하는 위치와 배열 인덱스가 같으면 인쇄
                    return answer
                heapq.heappop(heap) # 그렇지 않으면
                answer += 1 # answer += 1