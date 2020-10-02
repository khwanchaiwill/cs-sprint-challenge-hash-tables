def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    # loop through the list of array
    for array in arrays:
        #check the 

        for i in array:
            if i not in cache:
                cache[i] = 1
                
            else:
                cache[i] += 1
            
    for (num, count) in cache.items():
        if count == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
