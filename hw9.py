class Node:
    def __init__(this, label: str):
        this.links: list["Edge"] = []
        this.index = label

    def __str__(this):
        return 'Node ' + (str(this.index) or '?')

class Edge:
    def __init__(this, start: Node, end: Node, capacity: int, flow: int = None):
        if flow == None:
            flow = 0
        this.start: Node = start 
        this.end: Node = end 
        this.capacity: int = capacity 
        this.flow: int = flow

def DFS(start: Node, end: Node, seen: dict[Node, bool] = None, taken: list[Edge] = None, minAvailableCapacity: int = None) -> tuple[list[Edge], int]:
    if seen == None:
        seen = { start: True }
    if taken == None:
        taken = []
    if minAvailableCapacity == None:
        minAvailableCapacity = float('inf')

    # If we've hit our end node, then we don't need to keep looking
    if start == end:
        return [taken, minAvailableCapacity]
    for edge in start.links:
        if edge.start == start and not edge.start == edge.end:

            # If we find a path that we haven't seen yet and has available capacity, then take it
            if not seen.get(edge.end) and edge.capacity > 0:

                # Update our minimum available capacity when taking this edge
                minBefore = minAvailableCapacity
                minAvailableCapacity = min(minAvailableCapacity, edge.capacity)

                # Mark these nodes as seen and this edge as taken, so we don't end up in any cycles
                seen.update({edge.end: True})
                taken.append(edge)

                # If we found a valid path using this path choice, then use it (return it)
                ret = DFS(edge.end, end, seen, taken, minAvailableCapacity)
                if ret[0] != None:
                    return ret
                else:
                    taken.pop()
                    seen.update({edge.end: False})
                    minAvailableCapacity = minBefore

    # If we find no valid paths, then return None
    return [None, -1]

def PrintPath(path: list[Edge]):
    append = ''
    for edge in path:
        append += ' to ' + str(edge.end.index)
    print('Found path:', str(path[0].start.index) + append)

# First input will be num. of instances
for _ in range(int(input())):

    # Input afterwards will be number of nodes and number of edges in the graph
    numNodes, numEdges = [int(x) for x in input().strip().split()]
    graph: dict[int, Node] = {}

    for _ in range(numEdges):

        # Take in input for each edge: source node, dest. node, capacity
        sourceIndex, destIndex, capacity = [int(x) for x in input().strip().split()]

        # Ensure the nodes we want to reference exist, create them if they don't
        if not graph.get(sourceIndex):
            graph.update({sourceIndex: Node(sourceIndex)})
        if not graph.get(destIndex):
            graph.update({destIndex: Node(destIndex)})
        
        # See if we have any edges that already connect these two nodes
        preexisting: bool = False
        for edge in graph.get(sourceIndex).links:
            if edge.end == graph.get(destIndex):
                edge.capacity += capacity
                preexisting = True

        # Otherwise, Create the edge linking the two nodes
        if not preexisting:
            edge = Edge(graph.get(sourceIndex), graph.get(destIndex), capacity)
        
        graph.get(sourceIndex).links.append(edge)
        graph.get(destIndex).links.append(edge)

    # We want the maximum flow from node 1 to node n in this graph...
    totalflow = 0

    # While there's a path from s to t with available capacity
    x = DFS(graph.get(1), graph.get(numNodes))
    while(x[0] != None):

        # Now that we have a flow on G (x), we need to modify the edges to create a residual graph:
        flow: list[Edge] = x[0]
        amount: int = x[1]
        totalflow += amount

        # PrintPath(flow)
        # Make sure we have a valid flow just because
        if amount > 0 and len(flow) > 0:
            for edge in flow:

                # For every edge (u, v) in E, add edge (u, v) with capacity c_e - f(e), and...
                edge.capacity -= amount

                # Add edge (v, u) with capacity f(e) (first, find if an edge from v to u already exists)
                found = None
                for e in edge.end.links:
                    if e.end == edge.start:
                        found = e
                        break

                # If one does exist, then just adjust its capacity and flow
                if found != None:
                    found.capacity -= amount
                    found.flow += amount

                # Otherwise, create a new, reversed edge and set its capacity (remaining amt) to 0, and its flow to the amount of flow going backwards
                else:
                    newEdge = Edge(edge.end, edge.start, amount, amount)
                    edge.start.links.append(newEdge)
                    edge.end.links.append(newEdge)

        x = DFS(graph.get(1), graph.get(numNodes))
    
    print(totalflow)