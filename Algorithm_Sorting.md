###### 참고 : https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Algorithm

# Sorting Algorithm
-------------------
sorting 알고리즘은 Comparisons 방식과 Non-Comparisons 방식으로 나눌 수 있다.


## Comparisons Sorting Algorithm (비교 방식 알고리즘)

### Bubble Sort
인접한 두 개의 데이터를 비교해가면서 정렬을 진행하는 방식
가장 큰 값을 배열의 맨 끝에다가 이동시키면서 정렬함

Space Complexity : O(1)
Time Complexity : O(n^2)

<pre>
<code>
def BubbleSort(lst):
    lst_length = len(lst)

    for i in range(lst_length):
        for j in range(lst_length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

if __name__ == "__main__":
    lst = [2, 3, 1, 4]

    BubbleSort(lst)
    print(lst)
</code>
</pre>

