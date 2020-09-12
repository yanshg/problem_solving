#!/usr/bin/python

# the list is maybe sorted or almost sorted,

def bubble_sort(numbers):
    n=len(numbers)
    for i in range(n-1,1,-1):
        sorted=True
        for j in range(i):
            if numbers[j]>numbers[j+1]:
               numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
               sorted=False
        if sorted:
            break
    return numbers

numbers=[13, 6, 23, 67, 45, 92, 4, 53, 25, 7]
print("numbers: ", numbers)

bubble_sort(numbers)
print("after bubble sort, numbers: ", numbers)

numbers=[10, 20, 23, 67, 70, 92, 101, 153, 167, 700]
print("numbers: ", numbers)

bubble_sort(numbers)
print("after bubble sort, numbers: ", numbers)
