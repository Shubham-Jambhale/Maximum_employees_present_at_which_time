import heapq

def maxEmployees ( list1 , list2 ) :
    
    array = []
    count = 0
    #maintaining 2 heaps max heap and min heap
    heapq.heapify(list1)
    heapq.heapify(list2)
    
    #iterating over the heap
    while list1 and list2:
        
        elem1 = heapq.heappop(list1)
        elem2 = heapq.heappop(list2)
        
        #popping the elements from heap and checking which element is greater and increasing the max_counter count.
        
        if elem1 < elem2:
            count += 1
            array.append(count)
            heapq.heappush(list2,elem2)
        #if both times are equal we have to give preference to clockin  so increasing the counter.
        elif elem1 == elem2:
            count += 1
            array.append(count)
            heapq.heappush(list2,elem2)
        #decreasing count if clockout
        else:
            count -= 1
            array.append(count)
            heapq.heappush(list1,elem1)

    maximum = max(array)
    count = array.count(maximum)
    
    return (maximum,count)
