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