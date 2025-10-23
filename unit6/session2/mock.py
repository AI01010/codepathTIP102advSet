# problem 1
# Given a string s consisting of English letters (lowercase and/or uppercase) and digits, 
# return all possible strings that can be formed by changing the case of the letters in s. 
# You may not alter the order of characters in the string, and digits should remain unchanged.
# Input: s = "a1b2"
# Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
# Input: s = "3z4"
# Output: ["3z4", "3Z4"]Input: s = "12345"
# Output: ["12345"]

#U: 
# input s string 
# outputing all possible combination of the lower and uppercases of the alpha characters in that string at a list
# ?edge case empty string or no alpha char
# contraint cant alter order of string, and cant edit digits

#M: tolowercase to uppercase, combinations/permuatison (in order) problem

#P:  creat teh emoty list, add the init str s, then start making combos
#    count of alpha char
#    loop for count changing n number of letter 
#       changing == swap upper to lower or lower to upper
#       inrease n +1 unitl n=count of alpha char

def combinations(s):
    result = []
    alphaCount = 0
    num = 0 #num of changes
    tempS = ""

    #get count
    for ch in s:
        if ch.isalpha():
            alphaCount+=1
    
    #loop
    for i in range(len(s)):
        for n in range(num):
            if n > 0 and s[i].isalpha():
                if s[i].islower():
                    tempS = s[0:i] + s[i].upper() + s[i+1:]
                else:
                    tempS = s[0:i] + s[i].lower() + s[i+1:]
            result.append(tempS)
    

    return result

print(combinations("a1b2"))
print(combinations("3z4"))