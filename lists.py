def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 5:
        del list_to_remove_elements[5]
    elif len(list_to_remove_elements) > 4:
        del list_to_remove_elements[4]
    elif len(list_to_remove_elements) > 0:
        del list_to_remove_elements[0]
    return list_to_remove_elements
    
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def add_elements(list_to_add_elements):
    list_to_add_elements.append('Yellow')
    list_to_add_elements.insert(0, 'Pink')
    return list_to_add_elements
print(add_elements(['Red', 'Green', 'White', 'Black']))

def is_empty(list_to_check):
    return list_to_check == []
print(is_empty([]))
print(is_empty(['Red', 'Green', 'White', 'Black']))

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    else:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
print(check_lists(['Black', 'Pink', 'Red', 'Green', 'White'], ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))

def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][0:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify
print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
