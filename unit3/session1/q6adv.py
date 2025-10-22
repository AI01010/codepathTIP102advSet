# marking event timeline
# event and timeline strs and t string for '?'
# recreate timeline in string t until it matches string timeline
# repacle '?' with event until timeline is reached, can overlap
# You may use at most 10 * len(timeline) marks.

# go iteration by iteration, look for closest solution and builf off it by marking more


def mark_event_timeline(event, timeline):
    t = ['?'] * len(timeline)
    markcount = 0
    total_matched = 0
    listEvent = [] # holds iterations
     
    indexes = []
    i = 0
    j = 0
    k = 1

    while timeline not in listEvent:
        while i+k+len(event) <= len(timeline):
            print("loop start")
            #check cond.
            if markcount >= (10 * len(timeline)):
                return []
            
            #outofbounds check
            if i+len(event) > len(timeline):
                i = 0
            
            print(t)

            #replace at certain index i
            j = 0
            for ch in event:
                t[i+j] = ch
                j+=1
            markcount += 1

            print(t)

            #check if t made progress
            j = 0
            matches = 0
            for ch in t:   #counting number of matches found
                if ch == timeline[j]:
                    matches += 1
                    j += 1

            if matches > total_matched: #if progress made
                listEvent.append(t)
                indexes.append(i)

            i += k
        k += 1    
          
    print(indexes)
    return indexes


print(mark_event_timeline("abc", "ababc"))  
# print(mark_event_timeline("abca", "aabcaca")) 