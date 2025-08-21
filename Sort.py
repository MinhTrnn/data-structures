import random
def BBsort(arr):
    for count in range(len(arr)-1):
            for i in range(0,len(arr)-count-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

                else:
                    pass

    return arr

    

           
if __name__=='__main__':
    arr = list(range(1,31))
    random.shuffle(arr)
    print(arr)
    print(BBsort(arr))
    