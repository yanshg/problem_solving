#!/usr/bin/python

def binary_search(nums, search_num):
    low,high=0,len(nums)-1
    while (low <= high):
        mid=low+(high-low)//2
        mid_num=nums[mid]
        if search_num == mid_num:
           return mid
        elif search_num > mid_num:
           low=mid+1
        else:
           high=mid-1
    return -1

if __name__ == '__main__':
    nums=[1,4,7,9,12,15,23,45,56,78]
    search=78
    result=binary_search(nums,search)
    print("nums: ", nums)
    print("search: ", search)
    print("result: ", result)
