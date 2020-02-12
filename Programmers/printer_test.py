# test to change
# from queue import PriorityQueue
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# answer = 1

# 문제 직독직해 but location 반영이 어려움
#  Q = []
#  while len(priorities) > 1 :
#     # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
#         temp = priorities.pop(0)
#     # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
#         if temp < max(priorities) :
#             priorities.append(temp)
#     # 3. 그렇지 않으면 J를 인쇄합니다
#         else:
#             Q.append(temp)
#     Q.extend(priorities)

# testing
# Q = PriorityQueue()
# heap = []
# for i, v in enumerate(priorities):
    # Q.put((-v, i))

# while not Q.empty():
#     # answer = 1
#     print(Q.get())
#     # if Q.get()[1] == location :
#     #     # print(answer)
#     #     break
#     # answer += 1