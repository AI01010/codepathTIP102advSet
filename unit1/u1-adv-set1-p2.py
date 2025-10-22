#p2 2 pointer rev. list
# reverse an input string/any list
# initialize a head and tail pointer to swap the elements to the oppostie pointer
# move pointers from the end to the middle in 1 loop. tail pointer start from the list lenght - 1

def reverse_list(lst):
    
    #for i in range(len(lst)/2):
    i = 0
    j = len(lst)-1

    while i<=j:
        lst[i], lst[j] = lst[j], lst[i]
        i+=1
        j-=1

    print(lst)
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

lst = []
reverse_list(lst)