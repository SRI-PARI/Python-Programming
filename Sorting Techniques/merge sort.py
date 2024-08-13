def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        # Recursively sort both halves
        mergesort(left_side)
        mergesort(right_side)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_side
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_side
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

# Read input and call mergesort
arr = list(map(int, input().split()))
mergesort(arr)
print(arr)
