"""
a. transform_to_string that takes a list as a parameter and returns all its elements as a string.
For example for list [1, “hello“, True] the result should be → “1helloTrue“
"""
def transform_to_string(my_list):
    s = ""
    for element in my_list:
        s += str(element)
    print(s)

transform_to_string([1, "hello", True])


"""
b. get_unique_elements that takes a list as parameter and return list of only unique elements.
For list [1, 1, 2, True, True] the result should be → [1, 2, True]
"""
l = [1, 1, 2, 4, 4]

def get_unique_elements(numbers):
    p = []
    for item in numbers:
        if item not in p:
            p.append(item)
    print(p)

get_unique_elements(l)

"""
c. break_list_by_value that takes a list as a parameter, and another value as second parameter, and returns a tuple
 of the lists divided by the first instance of separator, if separator is not in the list return the list as tuple, 
 excluding separator. For example: break_list_by_value([1, 2, “a“, True], “a”) → ([1, 2], [True])
"""

def break_list_by_value(some_list, separator):
    if separator not in some_list:
        return some_list
    list_before = []
    list_after = []

    separator_found = False
    for element in some_list:
       if element == separator:
           separator_found = True
           continue
       if not separator_found:
           list_before.append(element)
       else:
           list_after.append(element)
    return (list_before, list_after)


print(break_list_by_value([1, 2, "a", True], "a"))






