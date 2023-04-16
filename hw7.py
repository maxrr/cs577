from math import ceil, floor

# Helper class to hold our variables - we could just use tuples but this makes it a little bit less confusing for my small brain
class Request:
    def __init__(self, start: int, finish: int, value: int):
        self.start: int = int(start)
        self.finish: int = int(finish)
        self.value: int = int(value)

    def __str__(self):
        return str(self.start) + ', ' + str(self.finish) + ', ' + str(self.value)


def Merge(A: list[Request], B: list[Request], param: str) -> list[Request]:
    S = []
    ai = 0
    bi = 0

    while ai < len(A) and bi < len(B):
        # if getattr(A[ai], 'finish') <= getattr(B[bi], 'finish'):
        if A[ai].finish <= B[bi].finish:
            S.append(A[ai])
            ai += 1
        else:
            S.append(B[bi])
            bi += 1

    if ai < len(A):
        S += A[ai:]
    elif bi < len(B):
        S += B[bi:]

    return S


def MergeSort(A: list[Request], param: str = 'finish') -> list[Request]:
    if len(A) > 1:
        half = floor(len(A) / 2)
        A1 = MergeSort(A[:half], param)
        A2 = MergeSort(A[half:], param)
        A = Merge(A1, A2, param)

    return A

# This works now too! (submission 8)
def BoundedBinarySearch(arr: list[Request], start: int, end: int, bound: int) -> int:
    # If we only have one element, then if it passes the bound return it, if not return -1
    if end <= start:
        return start if arr[start].finish <= bound else None

    mid = ceil((start + end) / 2)

    # If our midpoint is less than our bound, then only look at the right half
    if arr[mid].finish <= bound:
        return BoundedBinarySearch(arr, mid, end, bound)
    
    # Otherwise, only look at the left half
    else:
        return BoundedBinarySearch(arr, start, mid - 1, bound)

# This works! (submission 7)
def BoundedLinearSearch(arr: list[Request], end: int, bound: int) -> int:
    maxElemIndex = None 
    for i, elem in enumerate(arr):
        if i > end or elem.finish > bound:
            break
        maxElemIndex = i
    return maxElemIndex

# How many times we'll look for a list of jobs
instances = int(input())
for _ in range(instances):

    # How many jobs in this instance
    j = int(input())

    # Make an array to collect our jobs (requests)
    jobs: list[Request] = []

    # The input we're given will have finish time in ascending order, so we don't need to worry about sorting it, just start adding:
    for _ in range(j):
        line = input().strip().split()
        jobs.append(Request(*line))

    # Sort the jobs by finish time (asc)
    jobs = MergeSort(jobs)

    # for job in jobs:
    #     print(job)

    # Solution matrix, with m[0] = 0
    m = [0]

    for j, job in enumerate(jobs):
        # Find index i < j st. (finish of i) <= (start of j)
        # note: i here is just the value, because that's easier
        i = BoundedBinarySearch(jobs, 0, j - 1, job.start)
        # i = BoundedLinearSearch(jobs, j - 1, job.start) # (This works! Passes gradescope)
        m.append(max(m[j], m[(i + 1) if i != None else 0] + job.value))

    print(m[len(m) - 1])