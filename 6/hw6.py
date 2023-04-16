from MergeCount import MergeCount

if __name__ == '__main__':
    reps = int(input())
    for _ in range(reps):
        # Get the number of points we should read in
        numPoints = int(input())

        # Store the points we're going to be given
        points: list[int | tuple[int, int]] = []

        # Read points on top line 
        for i in range(numPoints):
            points.append(int(input()))

        # Read points on bottom line
        for i in range(numPoints):
            points[i] = [points[i], int(input())]

        # Sort the points we have by their first line entry
        points, _ = MergeCount(points, 0)

        # Count the number of inversions we have in the second line entry
        _, inv2 = MergeCount(points, 1)
        print(inv2)