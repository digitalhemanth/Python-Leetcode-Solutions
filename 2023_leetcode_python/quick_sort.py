def Quick_sort(arry):
    for a in range(len(arry)):
        for i in range(0, len(arry)-1):
            if arry[i] > arry[i+1]:
                arry[i] , arry[i+1] = arry[i+1], arry[i]
        print(arry) 
      
    return arry    
                        
arry = [2,8,4,1,-6,9,5]
Quick_sort(arry)



"""

There are numerous types of sorting algorithms, each with its own advantages, disadvantages, and specific use cases. Here are some commonly known sorting algorithms:

Bubble Sort: A simple comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order until the entire list is sorted. It has a time complexity of O(n^2) and is mainly used for educational purposes.

Selection Sort: Another simple algorithm that sorts the list by repeatedly finding the minimum element from the unsorted part and placing it at the beginning. It also has a time complexity of O(n^2) and is not suitable for large lists.

Insertion Sort: A comparison-based algorithm that builds the final sorted list one element at a time. It iterates through the list, comparing each element with the already sorted part and inserting it in the correct position. It has an average and worst-case time complexity of O(n^2), but it performs well for small lists or nearly sorted lists.

Merge Sort: A divide-and-conquer algorithm that recursively divides the list into two halves, sorts them independently, and then merges them to obtain the final sorted list. It has a stable time complexity of O(n log n) and is efficient for large lists, but it requires additional memory for the merging process.

Quick Sort: As mentioned earlier, Quick sort also follows the divide-and-conquer approach. It has an average time complexity of O(n log n) and is widely used due to its efficiency. However, in the worst case, it can have a time complexity of O(n^2).

Heap Sort: A comparison-based sorting algorithm that uses a binary heap data structure. It builds a max-heap from the list, repeatedly extracts the maximum element (root), and places it at the end of the sorted list. It has a time complexity of O(n log n) and is an in-place sorting algorithm.

Radix Sort: A non-comparison-based algorithm that sorts integers by grouping them by digits. It starts by sorting the least significant digit and progressively moves towards the most significant digit. Radix sort has a time complexity of O(kn), where k is the number of digits in the largest element.    
    
    """