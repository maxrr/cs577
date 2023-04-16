# Knapsack Implementation
# Figure out how many times we want to solve Knapsack
for _ in range(int(input())):

    # Figure out how many items we'll have, and our maximum weight
    numItems, W = (int(x) for x in input().strip().split())

    # Initialize empty solution matrix
    v: list[list] = []

    # For each element in this solution:
    for i in range(numItems):

        # Get the weight and value for this item
        weight, value = (int(x) for x in input().strip().split())
        
        # Add a new row to the solution matrix
        v.append([])

        # For each weight value for this item
        for w in range(W):

            # Bellman from lecture slides
            v[-1].append(max(v[i - 1][w] if i > 0 else 0, (1 if w >= (weight - 1) else 0) * ((v[i - 1][w - weight] if i > 0 and w >= weight else 0) + value)))
    
    # Print final value
    print(v[-1][-1] if len(v) > 0 and len(v[-1]) > 0 else 0)