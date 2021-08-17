def BubbleSort(lst):
    lst_length = len(lst)

    for i in range(lst_length):
        for j in range(lst_length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def SelectionSort(lst):
    for i in range(len(lst)-1):
        idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[idx]:
                idx = j
        lst[i], lst[idx] = lst[idx], lst[i]


def InsertionSort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


if __name__ == "__main__":
    lst = [2, 3, 1, 4]

    InsertionSort(lst)
    print(lst)