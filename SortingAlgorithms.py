from random import randint
import timing

ARRAY_LENGTH = 5000

def bubble_sort(list1):

# Swap the elements to arrange in order
   for iter_num in range(len(list1)-1,0,-1):
      for idx in range(iter_num):
         if list1[idx]>list1[idx+1]:
            temp = list1[idx]
            list1[idx] = list1[idx+1]
            list1[idx+1] = temp


def merge_sort(listmerge):
   if len(listmerge) <= 1:
      return listmerge
# Find the middle point and divide it
   middle = len(listmerge) // 2
   left_list = listmerge[:middle]
   right_list = listmerge[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

def insertion_sort(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
      # Compare the current element with next one
      while (InputList[j] > nxt_element) and (j >= 0):
         #print(f"j = {j} , InputList[j]= {InputList[j]}, nxt_Element = {InputList[i]}")
         InputList[j+1] = InputList[j]
         j=j-1
      InputList[j+1] = nxt_element

def shellSort(input_list):
   gap = len(input_list) // 2
   while gap > 0:
      for i in range(gap, len(input_list)):
         temp = input_list[i]
         j = i
         # Sort the sub list for this gap
         while j >= gap and input_list[j - gap] > temp:
            input_list[j] = input_list[j - gap]
            j = j-gap
            input_list[j] = temp
      # Reduce the gap for the next element
      gap = gap//2

def selection_sort(input_list):
   for idx in range(len(input_list)):
      min_idx = idx
      for j in range( idx +1, len(input_list)):
         if input_list[min_idx] > input_list[j]:
            min_idx = j
      # Swap the minimum value with the compared value
      input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


def quicksort(array):
   # If the input array contains fewer than two elements,
   # then return it as the result of the function
   if len(array) < 2:
      return array

   low, same, high = [], [], []

   # Select your `pivot` element randomly
   pivot = array[randint(0, len(array) - 1)]

   for item in array:
      # Elements that are smaller than the `pivot` go to
      # the `low` list. Elements that are larger than
      # `pivot` go to the `high` list. Elements that are
      # equal to `pivot` go to the `same` list.
      if item < pivot:
         low.append(item)
      elif item == pivot:
         same.append(item)
      elif item > pivot:
         high.append(item)


def insertion_sort_modified(array, left=0, right=None):
   if right is None:
      right = len(array) - 1

   # Loop from the element indicated by
   # `left` until the element indicated by `right`
   for i in range(left + 1, right + 1):
      # This is the element we want to position in its
      # correct place
      key_item = array[i]

      # Initialize the variable that will be used to
      # find the correct position of the element referenced
      # by `key_item`
      j = i - 1

      # Run through the list of items (the left
      # portion of the array) and find the correct position
      # of the element referenced by `key_item`. Do this only
      # if the `key_item` is smaller than its adjacent values.
      while j >= left and array[j] > key_item:
         # Shift the value one position to the left
         # and reposition `j` to point to the next element
         # (from right to left)
         array[j + 1] = array[j]
         j -= 1

      # When you finish shifting the elements, position
      # the `key_item` in its correct location
      array[j + 1] = key_item

   return array


def timesort(array):
   min_run = 32
   n = len(array)

   # Start by slicing and sorting small portions of the
   # input array. The size of these slices is defined by
   # your `min_run` size.
   for i in range(0, n, min_run):
      insertion_sort_modified(array, i, min((i + min_run - 1), n - 1))

   # Now you can start merging the sorted slices.
   # Start from `min_run`, doubling the size on
   # each iteration until you surpass the length of
   # the array.
   size = min_run
   while size < n:
      # Determine the arrays that will
      # be merged together
      for start in range(0, n, size * 2):
         # Compute the `midpoint` (where the first array ends
         # and the second starts) and the `endpoint` (where
         # the second array ends)
         midpoint = start + size - 1
         end = min((start + size * 2 - 1), (n - 1))

         # Merge the two subarrays.
         # The `left` array should go from `start` to
         # `midpoint + 1`, while the `right` array should
         # go from `midpoint + 1` to `end + 1`.
         left = array[start:midpoint + 1]
         right = array[midpoint + 1:end + 1]
         merged_array = merge(left,right)

         # Finally, put the merged array back into
         # your array
         array[start:start + len(merged_array)] = merged_array

      # Each iteration should double the size of your arrays
      size *= 2

   return array


def improved_insertion_sort(my_array):
   n = len(my_array)
   for i in range(1,n):
       insert_index = i
       current_value = my_array[i]
       for j in range(i-1, -1, -1):
           if my_array[j] > current_value:
               my_array[j+1] = my_array[j]
               insert_index = j
           else:
               break
       my_array[insert_index] = current_value


def radix_sort(myArray):

    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(myArray)
    exp = 1

    while maxVal // exp > 0:

        while len(myArray) > 0:
            val = myArray.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                myArray.append(val)

        exp *= 10

list1 = [-1,19,2,31,45,-6,11,121,27]
bubble_sort(list1)
print(list1)

unsorted_list = [64, -2, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))

list2 = [19,2,31,45,-30,11,121,27]
insertion_sort(list2)
print(list2)

list3 = [19,2,31,-45,0,30,11,121,27]
shellSort(list3)
print(list3)

l = [19,2,-31,45,30,11,121,27,8]
selection_sort(l)
print(l)



if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
   # timing.run_sorting_algorithm(algorithm="merge_sort", array=array)
   # timing.run_sorting_algorithm(algorithm="bubble_sort", array=array)
   # timing.run_sorting_algorithm(algorithm="insertion_sort", array=array)
   # timing.run_sorting_algorithm(algorithm="selection_sort", array=array)
    timing.run_sorting_algorithm(algorithm="shellSort", array=array)
   # timing.run_sorting_algorithm(algorithm="quicksort", array=array)
   # timing.run_sorting_algorithm(algorithm="timesort", array=array)
    timing.run_sorting_algorithm(algorithm="sorted", array=array)
    timing.run_sorting_algorithm(algorithm="improved_insertion_sort", array=array)
    timing.run_sorting_algorithm(algorithm="radix_sort", array=array)
