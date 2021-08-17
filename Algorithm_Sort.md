###### 참고 : https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Algorithm

# Sorting Algorithm
sorting 알고리즘은 Comparisons 방식과 Non-Comparisons 방식으로 나눌 수 있다.


## Comparisons Sorting Algorithm (비교 방식 알고리즘)

### Bubble Sort
인접한 두 개의 데이터를 비교해가면서 정렬을 진행하는 방식   
가장 큰 값을 배열의 맨 끝에다가 이동시키면서 정렬함

Space Complexity : O(1)   
Time Complexity : O(n^2)

<pre>
<code>
```python
def BubbleSort(lst):
    lst_length = len(lst)

    for i in range(lst_length):
        for j in range(lst_length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
```
</code>
</pre>



### Selection Sort
비교하고 있는 값의 index를 저장해다고 최종적으로 한번만 바꿔준다.   
하지만 여러 번 비교하는 것(연산)은 마찬가지이다.

Space Complexity : O(1)   
Time Complexity : O(n^2)

<pre>
<code>
```python
def SelectionSort(lst):
    for i in range(len(lst)-1):
        idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[idx]:
                idx = j
        lst[i], lst[idx] = lst[idx], lst[i]
```
</code>
</pre>



### Insertion Sort
i번째를 정렬 순서라고 하면, 0부터 i-1까지의 원소들은 정렬되어있다고 가정한다.    
i번째 원소와 i-1번째 원소부터 0번째 원소까지 비교하면서 정렬 순서를 맞춰준다(순서를 바꿔준다).   
-> 바깥 루프는 순방향, 안쪽 루프는 역방향으로 진행한다.

Space Complexity : O(1)   
Time Complexity : O(n^2)

<pre>
<code>
```python
def InsertionSort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
```
</code>
</pre>
