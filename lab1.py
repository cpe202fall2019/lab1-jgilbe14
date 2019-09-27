
def max_list_iter(int_list):
    if int_list == None: # raise ValueError if list is None
        raise ValueError

    if len(int_list) == 0: # return None if list is empty
        return None

    max = int_list[0] # intialize max to first entry in list

    for n in int_list: # iterate through list
        if n > max: # compare to max, if larger, set max equal to that value
            max = n
    return max

def reverse_rec(int_list, index = 0):
    if int_list == None: # raise ValueError if list is None
        raise ValueError

    list_length = len(int_list) # create variable for list length

    if index == list_length // 2: # if at the middle of the list, return the reversed list
        return int_list

    temp = int_list[index] # put value from index position in temporary variable
    
    # exchange the value from the lefthand side of the list, 
    # with the value from the corresponding position on the right hand side
    int_list[index] = int_list[(list_length - index) - 1]
    int_list[(list_length - index) - 1] = temp

    index += 1

    return reverse_rec(int_list, index) # return the modified list, and incremented index

def bin_search(target, low, high, int_list):
    if int_list == None: # raise ValueError if list is None
        raise ValueError

    mid_index = (low + high)//2 # find the (truncated) mid-index

    if int_list[mid_index] == target: # check whether the mid_index equals the target
        return mid_index # if so return the index value of the target

    # if high equals low AND given the previous test failed, the value is not contained in the list
    if high == low:
        return None

    if int_list[mid_index] > target: # if mid_index is greater than the target
        high = mid_index - 1 # adjust the "high" bound to one less than the mid_index
        return bin_search(target, low, high, int_list) # recursively call bin_search with new "high" bound

    if int_list[mid_index] < target: # if mid_index is smaller than the target
        low = mid_index  + 1 #adjust the "low" bound to one more than the mid_index
        return bin_search(target, low, high, int_list) # recursively call bin_search with new "low" bound
