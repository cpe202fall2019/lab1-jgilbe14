
def max_list_iter(int_list):
    if int_list == None:
        raise ValueError

    if len(int_list) == 0:
        return None

    max = int_list[0]

    for n in int_list:
        if n > max:
            max = n
    return max

def reverse_rec(int_list, index = 0):
    if int_list == None:
        raise ValueError

    list_length = len(int_list)

    if index == list_length // 2:
        return int_list

    temp = int_list[index]
    int_list[index] = int_list[(list_length - index) - 1]
    int_list[(list_length - index) - 1] = temp

    index += 1

    return reverse_rec(int_list, index)

def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError

    mid_index = (low + high)//2

    if int_list[mid_index] == target:
        return mid_index

    if int_list[mid_index] > target:
        high = mid_index
        return bin_search(target, low, high, int_list)

    if int_list[mid_index] < target:
        low = mid_index
        return bin_search(target, low, high, int_list)

    if high == low:
        return None
