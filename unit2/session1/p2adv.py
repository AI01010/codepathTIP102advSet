# message checker p2
# the function checks if a message conatins all the letters of the alphabet then boolean true, otherwise false
# contraints: only lowercase English letters and whitespace
# edge case: empty string, all whitespaces

# O(n) runtime complexity & O(1) space complexity


def can_trust_message(message):
    # trustable = False
    alphaArr = [0]*26 # map the alphabet

    for ch in message:
        if ch.isalpha():
            alphaArr[ord(ch)-ord('a')] += 1

    for i in alphaArr:
        if i <= 0:
            return False
        
    return True

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))


#set, remove a letter if found, if empty set stop or if end of string stop and evalute
