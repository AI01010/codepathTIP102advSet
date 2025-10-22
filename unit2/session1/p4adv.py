#disable booby trap
# find if the frequncy of each char. of a string is balanced after deleting 1 char. return a bool. if balance is possible wiht 1 rm
# constraint: given a string with almost even freq. except for 1 char. all lowercase letters
# edge: empty string, 1 letter case

# O(n) time - full traversal
# O(n) space  - map the whole string to a dict.

def can_make_balanced(code):
    freqMap = {}

    for ch in code:
        if ch in freqMap:
            freqMap[ch]+=1
        else:
            freqMap[ch]=1

    if sum(freqMap.values()) % 2:
          return True

    return False


code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
