from math import log, floor

class OptimizedNode:
    def __init__(this, label: int):
        this.links: dict[int, Edge] = {}
        this.index = label 
        this.orderedLinks: list[int] = []
    
    def __str__(this):
        return 'Node ' + (str(this.index) or '?')
    
    def addToOrderedLinks(this, index, capacity, start: int = None):
        if start == None:
            start = 0
        for (i, nodeIndex) in enumerate(this.orderedLinks, start):

            # If this entry's corresponding entry in `this.links` has a lesser
            # capacity than the link we're trying to add, then choose this spot
            if this.links.get(nodeIndex).capacity < capacity:
                this.orderedLinks.insert(i, index)
                return 
        
        # If we didn't find a lesser capacity, then this capacity must be the least, so add it at the end
        # This also functions as a failsafe if `this.orderedLinks` is empty
        this.orderedLinks.append(index)

    def updateEdge(this, e: "Edge"):
        index = e.end.index
        # If we're adding an edge for the first time (not just updating it), ...
        if not this.links.get(index, None):

            # Then insert into `this.orderedLinks` at the highest possible spot (first indices will have edges of maximum capacity)
            this.addToOrderedLinks(index, e.capacity)
        else:

            # Otherwise, remove the link and add it back (could probably optimize this with a heap)
            this.orderedLinks.remove(index)
            this.addToOrderedLinks(index, e.capacity)

        # Add/update the entry in `this.links`
        this.links.update({index: e})

class Edge:
    def __init__(this, start: OptimizedNode, end: OptimizedNode, capacity: int):
        this.start: OptimizedNode = start
        this.end: OptimizedNode = end
        this.capacity: int = capacity 

def OptimizedDFS(start: OptimizedNode, end: OptimizedNode, delta: int, seen: set[OptimizedNode] = None, taken: list[Edge] = None, minAvailableCapacity: int = None) -> tuple[list[Edge], int]:
    if seen == None:
        seen = set({start})
    if taken == None:
        taken = []
    if minAvailableCapacity == None:
        minAvailableCapacity = float('inf')

    # Go through and find a good starting path
    for entry in start.orderedLinks:
        edge = start.links.get(entry)

        # If we find a path that we haven't seen before...
        if not edge.end in seen:

            # Since the entries in `start.orderedLinks` are sorted, if we've hit 0 then the rest must also be 0 (or less than 0, but that *should* never happen)
            if edge.capacity == 0:
                return [None, 0]

            # ...mark it as seen
            seen.add(edge.end)
            taken.append(edge)

            if edge.end == end:
                return [taken, min(minAvailableCapacity, edge.capacity)]

            # Run DFS on the next level down, and if it gives us something good, then return it, otherwise set things back to the way they were and try the next path
            ret = OptimizedDFS(edge.end, end, delta, seen, taken, min(minAvailableCapacity, edge.capacity))
            if ret[0] != None:
                return ret
            else:
                taken.pop()
                seen.discard(edge)

    # If we can't find any paths, return that information
    return [None, 0]

def PrintPath(path: list[Edge]):
    append = ''
    for edge in path:
        append += ' to ' + str(edge.end.index)
    print('Found path:', str(path[0].start.index) + append)

def OptimizedMaxFlow(start: OptimizedNode, end: OptimizedNode, maxCapacity: int) -> int:
    totalflow = 0

    delta = max(floor(log(maxCapacity, 2)), 1)
    # print(maxCapacity, delta, 2^delta)

    while delta >= 1:
        # Find an initial path from s to t
        x = OptimizedDFS(start, end, delta)
        while x[0] != None:
            path: list[Edge] = x[0]
            amount: int = x[1]
            totalflow += amount 

            # If this path is valid, then...
            if amount > 0 and len(path) > 0:
                # For every edge (u, v) in our path...
                for edge in path:

                    # Add an edge with capacity c_e - f(e), and...
                    edge.capacity -= amount 
                    # edge.start.updateEdge(edge.end.index, edge)
                    edge.start.updateEdge(edge)
                    
                    # Add an edge (v, u) with capacity f(e)
                    existing = edge.end.links.get(edge.start.index, None)
                    if existing == None:
                        existing = Edge(edge.end, edge.start, 0)
                    existing.capacity += amount
                    edge.end.updateEdge(existing)
            else:
                break

            # Try again to find a path from s to t on our residual graph
            x = OptimizedDFS(start, end, delta)

        delta = delta / 2

    return totalflow 

# Only run this if we call the file directly
if __name__ == '__main__':

    # First input will be num. of instances
    for _ in range(int(input())):

        # Input afterwards will be number of nodes and number of edges in the graph
        numNodes, numEdges = [int(x) for x in input().strip().split()]
        graph: dict[int, OptimizedNode] = {}

        maxCapacity = 0

        for _ in range(numEdges):

            # Take in input for each edge: source node, dest. node, capacity
            sourceIndex, destIndex, capacity = [int(x) for x in input().strip().split()]

            # Ensure the nodes we want to reference exist, create them if they don't
            if not graph.get(sourceIndex):
                graph.update({sourceIndex: OptimizedNode(sourceIndex)})
            if not graph.get(destIndex):
                graph.update({destIndex: OptimizedNode(destIndex)})

            # See if we have any edges that already connect these two nodes, and if so, expand its capacity instead of making a whole new edge
            e = graph.get(sourceIndex).links.get(destIndex, None)
            if e == None:
                e = Edge(graph.get(sourceIndex), graph.get(destIndex), 0)
            e.capacity += capacity

            # Find the maximum capacity for delta
            maxCapacity = max(maxCapacity, e.capacity)

            graph.get(sourceIndex).updateEdge(e)

        print(OptimizedMaxFlow(graph.get(1), graph.get(numNodes), maxCapacity))