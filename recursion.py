def sum(list):
    """a: List(int)"""
    """r: int"""
    if list == []:
        return 0
    return list[0] + sum(list[1:])
def count(list):
    """list: List(any)"""
    """r: int"""
    if list == []:
        return 0
    return 1 + count(list[1:])

def find_max(list):
    """list: List(any)"""
    """r: int"""
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = find_max(list[1:])
    return list[0] if list[0] > sub_max else sub_max
    
print(find_max([1, 34, 2921, 349, 3981, 291]))
