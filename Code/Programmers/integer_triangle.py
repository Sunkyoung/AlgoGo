def solution(triangle):
    # best = [ [ 0 for row in range(len(triangle)) ] for j in range(len(triangle)) ] # 0으로 초기화
    # best = [ [ 0 ] * i for i in range(1,len(triangle)+1)  ] * len(triangle)  # 0으로 초기화 다른 방법
    # best[0][0] = triangle[0][0]
    
    # 배열을 별도로 사용하지 않고, triangle 배열에 값 업데이트하면서 진행
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0: # index out of array 처리하려고 조건 - 첫번째 원소일 때
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # 마지막 원소일 때
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])