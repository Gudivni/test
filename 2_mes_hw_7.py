# бинарный поиск

from random import choice
def binary_search(my_list, a):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if a == my_list[mid]:
            return mid
        elif a < my_list[mid]:
            return binary_search(my_list, mid - 1)
        else:
            return binary_search(my_list, mid + 1)


my_list = list(range(1, 101))
a = choice(my_list)
start = 0
stop = len(my_list)


print('значение', a, 'под индексом: ', my_list.index(a))


# Алгоритм сортировки пузырьком
def bubble_sort(b):
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if b[j] > b[j+1]:
                temp = b[j]
                b[j] = b[j+1]
                b[j+1] = temp

b = [1, 12,-2, 8, 5, 17, -4, 3, 7, -7, 2, 6, 9]
bubble_sort(b)
print(b)



