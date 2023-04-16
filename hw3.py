# This saves me from writing my own heap class! Yay!
import heapq

# Wrapper class to help us more easily access a job's details
class Job:
    def __init__(self, start: int, end: int):
        self.start = int(start)
        self.end = int(end)
    
    # This is what's needed to heapify this class
    def __lt__(self, other):
        return self.end < other.end

# Only do this stuff if this file is run as a script
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        # heap = [Job(1, 2), Job(3, 4), Job(2, 6), Job(2, 2)]
        # heapq.heapify(heap)

        # Make an un-heapified list of jobs for this set 
        jobs = []

        n = int(input())
        for _ in range(n):

            # Find the start and end times of our job
            line = input().split(" ")

            # Add this job to our list
            jobs.append(Job(line[0], line[1]))

        # Turn our list into a heap
        heapq.heapify(jobs)

        # Keep track of what time we're at (to see if items will be compatible)
        time = 0

        # Keep track of how many jobs we've been able to accept (this is the value to return)
        count = 0

        # Keep removing from the head until we can't anymore 
        while len(jobs) > 0:

            # Pop the top job (the one with the lowest finish time)
            # This should be O(1) since we've turned our list of jobs into a heap
            j = heapq.heappop(jobs)

            # If it's compatible, include it in our final list (we don't actually
            # need to make a list because we only care about the # of jobs)
            if j.start >= time:
                time = j.end
                count += 1

        print(count)