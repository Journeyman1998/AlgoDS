def heapifyUtil(arr, index):
        if 2*index+1 >= len(arr):
            return
        
        lc = 2*index+1
        rc = 2*index+2
        indexLargest = index
        largest = arr[index]

        if arr[lc] > largest:
            largest = arr[lc]
            indexLargest = lc
            
        if rc < len(arr) and arr[rc] > largest:
            largest = arr[rc]
            indexLargest = rc
        
        if indexLargest != index:
            arr[index], arr[indexLargest] = arr[indexLargest], arr[index]
            heapifyUtil(arr, indexLargest)

def heapify(arr):
    for i in range(len(arr)-1, -1, -1):
        heapifyUtil(arr, i)
    
    return arr

def heappop(arr):
    toRet = arr[0]

    arr[0], arr[-1] = arr[-1], arr[0]
    arr.pop()

    heapifyUtil(arr, 0)
    return toRet

def heappush(arr, x):
    arr.append(x)
    child = len(arr) - 1
    parent = (child-1)//2
    while arr[parent] < arr[child] and parent >= 0:
        arr[parent], arr[child] = arr[child], arr[parent]
        child = parent
        parent = (child-1)//2