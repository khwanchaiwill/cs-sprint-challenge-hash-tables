def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set dictionary
    cache = {}
    # create the empty array to store the result
    result = []
    # loop through list a 
    for num in a:
        # set the num in dictionaty
        cache[num] = num
        # if number not equal 0 and the negative number in dictionary
        if num != 0 and -num in cache:
            # add the abosolute sorted number in to array
            result.append(abs(num))    
        # then return the result array

    return result
    

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
