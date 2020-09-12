#!/usr/bin/python

# Article:  https://en.wikipedia.org/wiki/Quicksort

#
# Ways to choose pivot
#    1. The first element
#    2. The last element
#    3. The medium element
#
# Get position which (the number at the position NEED NOT be the pivot):
#     the low part <= pivot
#     the high part >= pivot
#


# Solution 1:  use midium element as pivot

def quick_sort1(nums,low,high):
    if low<high:
        index=partition1(nums,low,high)
        quick_sort1(nums,low,index-1)
        quick_sort1(nums,index,high)

# must use 'nums[low]<pivot' and 'nums[high]>pivot',
# otherwise, loop infinite.

def partition1(nums,low,high):
    pivot=nums[low + (high-low)//2]
    while low<=high:
        while nums[low]<pivot:
            low+=1
        while nums[high]>pivot:
            high-=1
        if low<=high:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1
    return low;


# Solution 2: use last element as pivot

def quick_sort2(nums,low,high):
    if low<high:
        index=partition2(nums,low,high)
        quick_sort2(nums,low,index-1)
        quick_sort2(nums,index+1,high)


#  |    <pivot   |               |
#  |-|-----------|-|-----------|-|
#  low           mid           high
#
def partition2(nums,low,high):
    pivot=nums[high]
    mid=low
    for i in range(low,high):
        if nums[i]<pivot:
            nums[mid],nums[i]=nums[i],nums[mid]
            mid+=1
    nums[mid],nums[high]=nums[high],nums[mid]
    return mid


if __name__ == '__main__':
    nums=[ 21, 14, 6, 51, 23, 7, 25, 23, 22, 33, 6, 44, 23, 15, 51, 76 ]
    nums1=nums[:]
    print("nums: ", nums)
    quick_sort1(nums, 0, len(nums)-1)
    print("nums after quick sort with midium element as pivot: ", nums)

    quick_sort2(nums1, 0, len(nums1)-1)
    print("nums after quick sort with last element as pivot:   ", nums1)
