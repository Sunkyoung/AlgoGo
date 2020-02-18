import math
def solution(brown, red):
    answer = []
    candidate = divisor(red) # red의 약수 구해서 가능한 조합 배열로 만들기
    for i,j in candidate:
        if (i+2)*(j+2) == (brown + red): # 갈색+레드 개수가 크기 곱셈 결과 값과 동일
            answer.append(i+2)
            answer.append(j+2)
            return answer
def divisor(red):
    temp = []
    length = int(math.sqrt(red))+1 # 루트값+1을 기점으로
    for i in range(1,length):
        if red % i == 0 : # 약수 찾기
            temp.append([red//i,i]) # 가로가 세로보다 길어야하므로, 큰 값을 가로값에 넣기
    return temp