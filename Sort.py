import random

def BBsort(arr):
    for count in range(len(arr)-1):
            is_swap = False
            for i in range(0,len(arr)-count-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    is_swap = True

                else:
                   pass

            if is_swap is False:
                break
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i +1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] ,arr[min_idx] = arr[min_idx], arr[i]

    return arr
        
 

           
if __name__=='__main__':
    arr = list(range(1,9))
    random.shuffle(arr)
    print(arr)
    print(selection_sort(arr))
    