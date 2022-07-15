
# Recursive Solution 
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy                                # We will use `deepcopy()` function from the `copy` module

def permute(inputList):
    
    # a compound list
    finalCompoundList = []                  # compoundList to be returned 
    
    # Set a base condition to terminate recursion function when the `inputList`
    # cannot be divided further and return the `finalCompoundList`
    
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        # We are going to split the input into two lists as follows:
        # `first_list` consisting of the first element on the `inputList`
        # `rest_list` consisting the remaining `inputList`
        
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        
        # Call the recursive function to split the `rest_list` further until it meets the base condition
        # and store the last `finalCompoundList` output into `sub_compoundList` variable
        
        sub_compoundList = permute(rest_list)
        
        # Once the recursion function meets the base condition, we can build the permutation by
        # iterating through all lists of the `compoundList` returned from previous recursive call
        
        for aList in sub_compoundList:
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList