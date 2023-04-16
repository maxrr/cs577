from math import floor

def Merge(A: list[tuple[int, int]], B:list[tuple[int, int]], param: int) -> tuple[list[tuple[int, int]], int]:
    S, c, ai, bi = [[], 0, 0, 0]

    while ai < len(A) and bi < len(B):
        if A[ai][param] <= B[bi][param]:
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

def MergeCount(A: list[tuple[int, int]], param: int = 0) -> tuple[list[tuple[int, int]], int]:
    if len(A) == 1:
        return [A, 0]
    
    half = floor(len(A) / 2)
    A1, c1 = MergeCount(A[:half], param)
    A2, c2 = MergeCount(A[half:], param)
    A, c = Merge(A1, A2, param)

    return [A, c + c1 + c2]