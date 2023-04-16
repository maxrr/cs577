from math import floor

def MergeCount(A: list, B:list) -> tuple[list, int]:
    S, c, ai, bi = [[], 0, 0, 0]

    while ai < len(A) and bi < len(B):
        if A[ai] <= B[bi]:
            S.append(A[ai])
            ai += 1
        else:
            c = c + len(A) - ai
            S.append(B[bi])
            bi += 1

    if ai < len(A):
        S += A[ai:]
    elif bi < len(B):
        S += B[bi:]

    return [S, c]

def CountSort(A: list) -> tuple[list, int]:
    if len(A) == 1:
        return [A, 0]
    
    half = floor(len(A) / 2)

    A1, c1 = CountSort(A[:half])
    A2, c2 = CountSort(A[half:])
    A, c = MergeCount(A1, A2)
    return [A, c + c1 + c2]

if __name__ == '__main__':
    reps = int(input())
    for _ in range(reps):
        input()
        line = input().strip().split()
        nums = [int(item) for item in line]
        _, inversions = CountSort(nums)
        print(inversions)