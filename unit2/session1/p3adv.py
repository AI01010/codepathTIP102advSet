#find duplicate lenghts
# array of chests on length 1-n each, find duplicates and return in an array of the duplicates only
# contraints: each integer appears once or twice, int array only
# edges: empty array, single element array

# O(n) time complexity - 1 loop thru 
# O(n) space complexity - mapping each element frequncy

def find_duplicate_chests(chests):
    duplicatesArr = []
    freqSet = set()

    for num in chests:
        if num in freqSet:
            duplicatesArr.append(num)
        freqSet.add(num)

    return duplicatesArr

#test
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))