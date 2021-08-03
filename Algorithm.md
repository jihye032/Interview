###### 참고 : https://github.com/JaeYeopHan/Interview_Question_for_Beginner


### 주요 알고리즘
  - Sorting (+ searching / binary search)
  - divide and Conquer
  - Dynamic programming / Memoization
  - Greediness
  - Recursion
  - Algorithms associated with a specific data structure (which brings us to our fourth suggestion..)

### 데이터 구조
  - array
  - stack / queue
  - hashset / hashmap / hashtable / dictionary
  - tree / binary tree
  - heap
  - graph
</br>
</br>

#문제 해결을 위한 전략적 접근
----------------------------
### 코딩 테스트의 목적
   1. 문제 해결 여부
   2. 예외 상황과 경계값 처리
   3. 코드 가독성과 중복 제거 여부 등 코드 품질
   4. 언어 이해도
   5. 효율성
 -> 궁극적으로는 문제 해결 능력을 측정하기 위함이며 이는 '어떻게 이 문제를 창의적으로 해결할 것인가'를 측정하기 위함이라고 볼 수 있다.
 
### 해결 방법 분류
#### Dynamic Programming (동적 계획법)
  복잡한 문제를 간단한 여러 개의 하위 문제로 나누어 푸는 방법을 말한다.
  * top-down : 여러 개의 하위 문제로 나눴을 시에, 하위 문제를 결합하여 최종적으로 최적해를 구한다.
    - 같은 하위 문제를 가지고 있는 경우가 존재. 최적해를 저장해서 사용하는 경우 하위 문제수가 기하급수적으로 증가할 때 유용. -> memoization이라 함
  * bottom-up : top-down 방식과는 다르게 하위 문제들로 상위 문제의 최적해를 구한다.
  
  예시 ) Fibonacci 수열
  <pre>
  <code>
  # top-down
  # 실행 시간 : O(1.6^n)
  def fibonacci(n):
    if n==1:
      return 1
    elif n==2:
      return 1
    else :
      return fibonacci(n-1) + fibonacci(n-2)
  </code>
  </pre>
  
  <pre>
  <code>
  # bottom-up
  # 실행 시간 : O(n)
  f = [0] * 51
  f[0] = 0
  f[1] = 1
  f[2] = 1
  
  def fibonacci(n):
    if ( f[n] > 0 ) :
      return f[n]
    else :
      f[n] = fibonacci(n-1) + fibonacci(n-2)
      return f[n]
   </code>
   </pre>
  
  ##### 접근 방법
    1. 모든 답을 만들어보고 그 중 최적해의 점수를 반환하는 완전 탐색 알고리즘을 설계한다.
    2. 전체 답의 점수를 반환하는 것이 아니라, 앞으로 남은 선택들에 해당하는 점수만을 반환하도록 부분 문제 정의를 변경한다.
    3. 재귀 호출의 입력 이전의 선택에 관련된 정보가 있다면 꼭 필요한 것만 남기고 줄인다.
    4. 입력이 배열이거나 문자열인 경우 가능하다면 적절한 변환을 통해 메모이제이션(memoization) 할 수 있도록 조정한다.
    5. memoization을 적용한다.
    
  ###### memoization (메모이제이션)
  동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술
  동적 계획법의 핵심이 되는 기술이다.
    
  bottom-up 방식에서 볼 수 있듯이,  f[n]의 값을 계산하자마자 저장하면 실행 시간을 O(n)으로 줄일 수 있다.
  
#### Greedy (탐욕법)
  각 단계마다 지금 당장 가장 좋은 방법만을 선택하는 해결 방법
  많은 경우 최적해를 찾지 못하고 적용될 수 있는 경우가 두 가지로 제한 된다.
    
  1.탐욕법을 사용해도 항상 최적해를 구할 수 있는 경우
  2.시간이나 공간적 제약으로 최적해 대신 근사해를 찾아서 해결하는 경우
    
  #####접근 방법
  1. 문제의 답을 만드는 과정을 여러 조각으로 나눈다.
  2. 각 조각마다 어떤 우선순위로 선택을 내려야 할지 결정한다. 작은 입력을 손으로 풀어본다.
  3. 다음 두 속성이 적용되는지 확인해본다.
    
  1. 탐욕적 선택 속성 : 항상 각 단계에서 우리가 선택한 답을 포함하는 최적해가 존재하는가
  2. 최적 부분 구조 : 각 단계에서 항상 최적의 선택만을 했을 때, 전체 최적해를 구할 수 있는가
 
    


