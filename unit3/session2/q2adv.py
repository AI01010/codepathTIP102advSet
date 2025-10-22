# tallest skyscapper

# going in order adding total when we can't add any more floors (when we hit a higher number)

#O(n) time, O(1) space

def build_skyscrapers(floors):
    if len(floors) == 0:
        return 0
    
    totalSkyscrapers = 1

    for i in range(len(floors)-1):
        if floors[i+1] > floors[i]:
            totalSkyscrapers +=1

    return totalSkyscrapers

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9, 7, 3, 5, 1, 10, 3])) 

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

