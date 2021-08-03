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
#### DP(동적 계획법)
  복잡한 문제를 간단한 여러 개의 하위 문제로 나누어 푸는 방법을 말한다.
  * top-down : 여러 개의 하위 문제로 나눴을 시에, 하위 문제를 결합하여 최종적으로 최적해를 구한다.
    - 같은 하위 문제를 가지고 있는 경우가 존재. 최적해를 저장해서 사용하는 경우 하위 문제수가 기하급수적으로 증가할 때 유용. -> memoization이라 함
  * bottom-up : top-down 방식과는 다르게 하위 문제들로 상위 문제의 최적해를 구한다.
  
  예시 ) Fibonacci 수열
  <pre>
    <code>
      # top-down
      f (int n) {
        if n==0 : return 0
        elif n==1 : return 1
        
        if dp[n] has value : return dp[n]
        else : dp[n] = f(n-2) + f(n-1)
              return dp[n]
      }
    </code>
  </pre>
  
  


