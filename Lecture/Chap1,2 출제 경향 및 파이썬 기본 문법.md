# Part1,2 출제 경향 및 파이썬 기본 문법

### **최빈 문제 유형**

- 그리디, 구현, DFS/BFS

---

### **알고리즘 성능 평가**

복잡도 : 알고리즘의 성능을 나타내는 척도

- **시간 복잡도**: 특정 크기 입력에 대한 알고리즘의 **수행시간** 분석
- **공간 복잡도**: 특정 크기 입력에 대한 알고리즘의 **메모리 사용량** 분석

빅오 표기법 : 가장 빠르게 증가하는 항만을 고려하는 표기법으로, 함수의 상한만을 나타나게 됨

- 데이터의 크기 : N

    $O(2^n) < O(N^3) < O(N^2) < O(NlogN) < O(N) < O(logN) < O(1)$ 

**설계 Tip** 


코딩 테스트에서 시간제한은 통상 1~5초 가량

연산횟수가 5억이 넘어가는 경우,  Python 기준으로 통상 5-15초 시간 소요. 
( [PyPy](https://www.pypy.org/features.html)의 경우 때때로 C언어보다 빠르게 동작하므로, 지원 가능하다면 사용하자!)

<br>

**알고리즘 설계**

문제에서 가장 먼저 확인해야 하는 내용은 **시간제한(수행시간 요구사항)**

시간제한이 1초일 경우, 일반적인 기준은 다음과 같다.

- N의 범위가 500 : 최소 시간복잡도 $O(N^3)$
- N의 범위가 2,000 : 최소 시간복잡도 $O(N^2)$
- N의 범위가 100,000 : 최소 시간복잡도 $O(NlogN)$
- N의 범위가 10,000,000 : 최소 시간복잡도 $O(N)$

일반적인 알고리즘 문제 해결 과정 : 지문 읽기 → 요구사항(복잡도) 분석 → 문제 풀기 위한 아이디어 → 소스코드 설계 및 코딩

핵심 아이디어를 캐치한다면, 간결하게 소스코드를 작성할 수 있는 형태로 문제를 출제

---

### **자료형**

- 정수형
- 실수형

    IEEE754 표준에서는 실수형 저장을 위해 4바이트 혹으 8바이트의 고정된 메모리 할당하므로, 실수 정보 표현에 한계를 가짐. 하지만 10진수 체계에서는 2진수에 대한 정확히 표현이 가능

    → 이럴 때는 round() 함수 이용 

    e.g. 123.456 셋째자리에서 반올림 : `round(123.456,2)` → return 123.46

- 리스트 : **데이터를 연속적으로 담아 처리**하기 위해 사용하는 자료형

    곱셈 형태로 리스트 생성 가능

    e.g. [0] * 4 → [0, 0, 0, 0]

    인덱싱과 슬라이싱

    list comprehension : 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화하여 간결하게 표현 가능

    → 2차원 리스트 초기화할 때 효과적으로 사용 가능

    e.g. n x m 크기의 2차원 리스트일 때 n = 4, m = 3

    `array = [[0] * m for _ in range(n)]`

    [[0] * m] * n → 이렇게 한다면 전체 리스트 안에 포함된 n개의 각 리스트가 모두 같은 객체로 인식됨

    **Methods**

    | Name | Usage | Time Complexity |
    | :---: | :--------: | :------: |
    | append()| list.append() | O(1) |
    | sort() | lst.sort() / lst.sort(reverse=True) | O(NlogN) |
    | reverse()	| lst.reverse()	| O(N) |
    | insert() | list.insert(idx, value) | O(N) |
    | count() | list.count(value) | O(N) |
    | remove() | list.remove(value) | O(N) |

- 문자열
- 튜플

    리스트에 비해 상대적으로 **공간 효율적**

    **언제 사용하면 좋을까?**
    - 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
    - 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
    - 리스트보다 메모리 효율적으로 사용해야 할 때

- 사전 자료형

    파이썬에서 사전 자료형은 해시 테이블을 이용하므로 **데이터 조회 및 수정에 있어서 O(1) 시간에 처리 가능**

- 집합 자료형

    중복 허용하지 않고, 순서가 없음

    **데이터 조회 및 수정에 있어서 O(1) 시간에 처리 가능**

    연산 : 합집합(`a|b`) 교집합(`a&b`) 차집합(`a-b`)

    methods

    ```python
    data = set([1,2,3])
    # 원소 추가
    # {1,2,3,4}
    data.add(4)

    # 원소 여러개 추가
    # {1,2,3,4,5,6}
    data.update([5,6])

    # 특정 값을 갖는 원소 삭제
    # {1,2,4,5,6}
    data.remove(3)
    ```

    ⇒ 리스트나 튜플은 순서가 있기 때문에 인덱싱으로 값을 얻을 수 있는 반면, 사전형과 집합 자료형은 순서가 없기 때문에 인덱싱 대신 사전의 key 혹은 집합의 원소(element)를 이용해 O(1)의 시간 복잡도로 조회한다.

---

### **입출력**

입력

- input() : 한 줄의 문자열 입력
- map() : 리스트의 모든 원소에 각각 특정 함수 적용 시 사용

    공백을 기준으로 구본된 데이터 입력을 받을 때 사용

    e.g. `data = list(map(int, input().split()))`

    데이터의 개수가 많지 않고, 정해진 경우에 사용

    e.g. `a, b, c = map(int, input().split())`

- `sys.stdin.readline()` : 입력을 최대한 빠르게 받아야하는 경우에 사용. sys 라이브러리 필요

    단, 입력 후의 enter가 줄 바꿈 기호로 입력되므로 `rstrip()` 함께 사용

    → 이진탐색, 정렬, 그래프에 사용

출력

- print() : 기본적으로 출력 이후에 줄바꿈 수행

    end 속성을 통해 변경 가능 e.g. `print(a, end=" ")`

    f-string 문법 : python 3.6 부터 사용 가능

---

### **조건문과 반복문**

조건문 : 프로그램 흐름을 제어하는 문법

- `pass` 키워드 : 아무것도 처리하고 싶지 않을 때 사용 → debugging 시에 주로 사용

```python
if a > 90:
	pass
else:
	print('fail')
```

- python의 경우, 수학의 부등식 그대로 사용 가능

    `if x > 0 and x < 20`  == `if 0 < x < 20`

반복문 : 특정 소스코드를 반복적으로 실행하고자 사용하는 문법

- for문, while문 중 for문이 간결하게 표현 가능한 경우가 좀 더 있음 (but not always)

---

### **함수와 람다 표현식**

함수 : 특정 작업을 하나의 단위로 묶어놓은 것

- 내장 함수 : 파이썬 기본 제공 함수
- 사용자 정의 함수 : 개발자가 직접 정의한 함수
- `global` 키워드: global 변수

람다 표현식 : 함수를 간단하게 작성할 수 있음. 즉, 특정 기능을 수행하는 함수를 한 줄에 작성 가능

→ lambda 매개변수: 반환값

```python
def add(a, b):
	return a + b
# 일반적인 함수 사용
add(3, 7)
# 람다 표현식 사용
(lambda a, b: a + b)(3, 7)

array = [('홍길동', 50),('이순신', 32),('아무개', 74)]
# 내장 함수에서 자주 사용되는 예
sorted(array, key=lambda x: x[1])

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# 여러 개 리스트에 적용
map(lambda a, b: a + b, list1, list2)
```

---

### **자주 사용되는 표준 라이브러리**

- 내장 함수 : 기본 입출력 ~ 정렬함수

    `sum(), min(), max(), eval(), sorted()`

    - eval() : 수식으로 표현된 문자열을 계산한 값

        e.g. `result = eval("(3+5)*7")`

    - sorted() : 반복 가능한 객체에 대해 사용

        reverse와 key 속성이 있음. `reverse=True` 이면 내림차순 정렬!

        `sorted(array, key=lambda x: x[1], reverse=True)`

- **itertools** : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들. **완전 탐색에 유용하며 특히, 순열과 조합** 라이브러리는 코딩 테스트에서 자주 사용된다.

    모든 경우의 수를 고려해야 할 때,

    순열( $_{n}\mathrm{P}_{r}$ ): 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것

    조합( $_{n}\mathrm{C}_{r}$ ): 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 

    ```python
    from itertools import permutations, combinations, product, combinations_with_replacement
    data = ['A','B','C']
    # 순열
    result = list(permutations(data, 3))
    # 조합
    result = list(combinations(data, 2))
    # 중복 순열
    result = list(product(data, repeat=2))
    # 중복 조합
    result = list(combinations_with_replacement(data, 2))
    ```

- **heapq** : Heap 자료구조로, **우선순위 큐** 기능 구현을 위해 사용됨
- **bisect** : **이진 탐색** 기능 제공
- **collections** : deque, counter 등 유용한 자료구조 포함

    Counter: 등장 횟수를 세는 기능. 반복 가능한 객체에 대해 내부의 원소가 몇 번씩 등장했는지 알려줌

    ```python
    from collections import Counter
    counter = Counter(['a','b','a','c','b','b'])
    counter['b'] # return 3
    dict(counter) # {'a': 2, 'b': 3, 'c': 1}
    ```

- **math** : 필수적인 수학적 기능 제공. 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 ~ pi 와 같은 상수 포함

    최대 공약수와 최대 공배수

    ```python
    import math

    # 최대 공약수
    math.gcd(21, 14)

    # 최대 공배수
    def lcm(a, b):
    	return a * b // math.gcd(a,b)

    lcm(21, 14)
    ```