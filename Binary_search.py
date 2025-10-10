import time

lst = [1,2,3,56,89,456,786,1546]
lst.sort()

def BinSearch(target, lst):
    high = len(lst)-1
    low = 0
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        
        if lst[mid] == target:
            return mid
        
        elif lst[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
    
    return -1

target = 456

start = time.time()
result = BinSearch(target, lst)
end = time.time()

if result != -1:
    print("Element is present at index", result)
    print(lst[result])
    print(f"Time taken: {end - start} seconds")
else:
    print("Element is not present in array")
    print(f"Time taken: {end - start} seconds")
