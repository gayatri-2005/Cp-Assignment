'''Given two sorted arrays, merge them to get another sorted array
Example Input:
5     #size of first array
2 4 11 17 91      #first array
 
 4       #size of second array
 3 7 9 100 #second array
Example Output :
2 3 4 7 9 11 17 91 100
'''

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Example Input
arr1 = [2, 4, 11, 17, 91]
arr2 = [17, 91, 100]
print(merge_sorted_arrays(arr1, arr2))