class Node:
    def __init__(self, label, adjacent):
        self.label = label
        self.adjacent = adjacent
    
    def __str__(self):
        return f"{self.label}: [{self.adjacent}]"

# Recursive function to print out our nodes
def rec_print(nodes, qa, visited):

    # Output string for this recursive function
    output = ""

    while len(nodes) > 0:
        node = nodes.pop(0)

        # Look up in our QA table if the node is just a reference and not a root node
        if (type(node) == str):
            node = qa[node]

        # If we haven't visited this node before, then...
        if node.label not in visited:

            # Mark it as visited
            visited[node.label] = True

            # Print its label
            output += node.label + " "

            # Recurse on its adjacent nodes
            output += rec_print(node.adjacent, qa, visited)

    return output

# Input number of instances that follow
t = int(input())
for i in range(t):

    # Input number of nodes in the graph
    n = int(input())
    nodes = []
    nodesQA = {}

    # Populate the graph
    for x in range(n):

        # Find our inputs
        line = input().split()

        # Create the new node from this line and put it in our graph
        node = Node(line[0], line[1:])
        nodes.append(node)
        nodesQA[line[0]] = node

    # Recurse on the beginning nodes and print
    print(rec_print(nodes, nodesQA, {}).strip())