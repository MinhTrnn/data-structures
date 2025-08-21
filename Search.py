def Linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_searchh(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return mid
        elif target < mid[arr]:
            right = mid - 1
        elif target > mid[arr]:
            left = mid + 1

    return -1          
        



if __name__=='__main__':
    arr = [4,1,8,7,6,5,3,2]
    target = 7
    rs = Linear_search(arr,target)
    if rs != -1:
        print('found')
    else:
        print('not found')

