
#u - find all connecting flighte/node
#p - check each node as we get it if its connected ndoes cna connect back

def bidirectional_flights(flights):
    #base case if nodes connecting nodes can connect back
    for i in range(len(flights)):
        lst = flights[i]
        for j in lst:
            if i not in flights[j]:
                return False
    
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))