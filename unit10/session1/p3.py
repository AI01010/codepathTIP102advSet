#U - provide all flights possible from current location in order of most direct to most layovers needed
#P - start adding the target/current locations values/connect ports to a lst 
# then add its values's value or 2nd conenct ports via layover (if not already in the lst)
# go in order to keep ascending order consistency

from collections import deque

def get_all_destinations(flights, start):
    destination_lst = [] #set()
    destination_lst.append(start)

    queue = deque()
    queue.append(start)

    while queue:
        for i in range(len(queue)):
            loc = queue.popleft()
            for node in flights[loc]:
                if node not in destination_lst:
                    destination_lst.append(node)
                    queue.append(node)
    
    return destination_lst

    

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))