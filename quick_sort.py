def quicksort(array):
  """array: List[int]"""
  """rtype: List[int]"""
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if <= pivot]

    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
 
