def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache= {}

    # if len(weights) <= 1:
    #     return None
    for index in range(length):
        cache[weights[index]] = index
        
    return None
