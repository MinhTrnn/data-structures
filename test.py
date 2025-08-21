arr = [1,3,4,5,7,8,9,12,14,15]
def binary_searchh(arr, target):
    left = 0
    right = arr[-1]
    while left <= right:
        mid = (left + right) // 2
        print('mid:',mid)
        if target < arr[mid]:
            left = right - 1
            print('left:',left)
        elif target > arr[mid]:
            right = mid - 1
            print('mid:',mid)
    return -1          
        

print(binary_searchh(arr,9))