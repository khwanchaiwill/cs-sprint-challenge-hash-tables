#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # sett the list route slot to store the key and value
    route = [None] * length
    # check through the tickets key 
    for ticket in tickets:
        #set the 
        cache[ticket.source] = ticket.destination
    # set the next destination 
    next_des = cache["NONE"]

    for index in range(length):
        route[index] = next_des
        next_des = cache[next_des]
    return route
