import time
import numpy as np

def common_elems_num1(subset_elements, all_elements):
    ''' 
    returns a tuple of the number of common elements and time taken using sets

    subset_elements, all_elements: list
    '''
    
    # records the starting time to calculate the time taken for implementation
    start = time.time()

    #converting the lists to set for implementing the intersection function
    subset_elements = set(subset_elements)
    all_elements = set(all_elements)

    #intersection - returns all the common elements in both the list as a new set
    verified_elements = subset_elements.intersection(all_elements)
    
    # duration is calculated and printed
    duration = time.time() - start

    return (len(verified_elements), duration) 

def common_elems_num2(subset_elements, all_elements):
    ''' 
    returns a tuple of the number of common elements and time taken using NumPy

    subset_elements, all_elements: list
    '''
    # records the starting time to calculate the time taken for implementation
    start = time.time()

    # an array of all the common elements is stored in verified_elements
    verfied_elements = np.intersect1d(subset_elements,all_elements) 

    # recording the time taken
    duration = time.time() - start

    return len(verfied_elements), duration

def common_elems_num3(subset, all_elements):
    '''
    returns a tuple of the number of common elements and time taken using the traditional comparison using for loop

    subset_elements, all_elements: list
    '''

    #the time when the execution begins
    start = time.time()
    #an empty list to store the common elements from both the lists
    verified_elements = []

    for element in subset:
        # looping through subset
        if element in all_elements:
            # checking if 'element' is present in 'all_elements' and appending to verified_elements
            verified_elements.append(element)
    
    #calculate duration
    duration = time.time() - start
    return len(verified_elements), duration


if __name__ == "__main__":
    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    
    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')
    #lines in the files are split and stored into the lists
    
    print("Number of elements and time taken in s for three different approaches")
    print("First approach: Using NumPy")
    print(common_elems_num1(subset_elements, all_elements ))
    print("\nSecond approach: Using Set")
    print (common_elems_num2(subset_elements, all_elements ))
    print("\nThird approach: Using traditional for loop and comparing")
    print (common_elems_num3(subset_elements, all_elements ))