# This works but it times out
# Helper class!
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
# Get number of instances
reps = int(input())
for _ in range(reps):
    # Get number of pages for this instance
    p = int(input())
    req_count = input()

    # Instantiate pages in cache
    pages = {}

    # Get all given numbers
    line = input().strip().split(' ')

    # Populate a dictionary that will hold the next entry of every input value
    # to `line` (this will help us figure out which page to evict next)
    lastEntries = {}
    for i, num in enumerate(line):
        if not num in lastEntries:
            lastEntries[num] = Node(i)
        else:
            cur = lastEntries[num]
            while (cur.next):
                cur = cur.next
            cur.next = Node(i)

    # Set up a counter
    faults = 0

    # Start processing requests
    for i, num in enumerate(line):

        # If we don't already have this request stored in a cache page
        if not num in pages:
            faults += 1
            # If we have an empty cache page, then just chuck it in there
            if len(pages) < p:
                pages[num] = True

            # If not, then we need to evict
            else:
                # Find the stored item that has the furthest request in the future
                maxFound = None
                for page in pages:
                    # Ensure that we only find entries that will actually happen in the future
                    while (lastEntries[page] and i > lastEntries[page].val):
                        lastEntries[page] = lastEntries[page].next

                    # If the value we're looking at never has any more requests, then replace it
                    if not lastEntries[page]:
                        maxFound = page
                        break

                    # If this value should be our new FIF, then set it
                    if not maxFound or lastEntries[page].val > lastEntries[maxFound].val:
                        maxFound = page

                mf = str(maxFound)

                # Delete the FIF value we found from the cache (eviction)
                del pages[mf]

                # Increment its entry in lastEntries so we have fast lookups next time
                if lastEntries[mf]:
                    lastEntries[mf] = lastEntries[mf].next

                # Add our new value to the cache
                pages[num] = True

    # Print out the eviction counter we've been keeping track of 
    print(faults)