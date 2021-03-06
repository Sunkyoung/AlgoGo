# Chap3,4 Greedy & 구현

### **Greedy algorithm**

**현재 상황에서 지금 당장 좋은 것만 고르는 방법**을 의미한다.

이 방법은 **정당성 분석**이 중요하다. 즉, 단순히 가장 좋아 보이는 것을 반복적으로 선택해 최적의 해를 구할 수 있는 지 검토한다.

하지만, 일반적인 상황에서 최적의 해를 보장할 수 없을 때가 많다.

코딩테스트에서의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 이를 추론할 수 있어야 풀리도록 출제된다.

---

### **구현: 시뮬레이션과 완전 탐색**

**머릿속에 알고리즘을 소스코드로 바꾸는 과정**으로, 흔히 알고리즘 대회에서 해당 유형은 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭한다.

구현 유형의 예시는 다음과 같다.

- 알고리즘은 간단한데, 코드가 지나칠 만큼 길어지는 문제
- 실수연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제 → 특히 순열과 조합

int 자료형 데이터의 개수에 따른 메모리 사용량
| 데이터의 개수 (리스트의 길이) | 메모리 사용량 |
| :-------: | :----: |
| 1,000 | 4KB |
| 1,000,000 | 4MB |
| 10,000,000 | 40MB |

알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용된다. 해당 유형 문제에서는 2차원 공간에서의 **방향 벡터**가 자주 활용 된다.

![direction_vector](https://user-images.githubusercontent.com/26458213/124682914-eafa4480-df06-11eb-826a-2b3ffbce00c4.png)

```python
# 5 x 5 행렬에서의 이동

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2,2

for i in range(4):
	nx = x + dx[i]
	ny = y + dy[i]
```

**완전 탐색(Brute Forcing)** 문제 유형 : 가능한 경우의 수를 모두 검사해보는 탐색 방법