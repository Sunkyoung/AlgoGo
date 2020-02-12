# java to python
import heapq
def solution(priorities, location):
    answer = 1
    heap = []
    for i, v in enumerate(priorities):
        heapq.heappush(heap,-v)
    while heap:
        for i in range(len(priorities)) :
            if priorities[i] == -heap[0]:
                if i == location:
                    return(answer)
                heapq.heappop(heap)
                answer += 1