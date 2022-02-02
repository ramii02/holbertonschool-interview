#!/usr/bin/python3

# queue to add the keys as they open
# list to add the keys as u use them from the queue
# once queue is empty
# compare list of keys to the lenght of the array
# if they are the same, then return true
# if false then return false.

def canUnlockAll(boxes):
    #list of keys from each box.
    if len(boxes) == 0:
        return False
    key_list = set([0])
    #queue of keys to open box.
    key_ring = []
    key_ring.extend(boxes[0])
    while key_ring:
        key = key_ring.pop()
        if key <= len(boxes):
            if key not in key_list:
                key_list.add(key)
                key_ring.extend(boxes[key])
    if len(key_list) == len(boxes):
        return True
    else:
        return False


        