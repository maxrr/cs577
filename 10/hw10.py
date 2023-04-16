from hw9_opt import OptimizedNode, Edge, OptimizedMaxFlow

if __name__ == '__main__':
    for _ in range(int(input())):
        # Get input for number of nodes in set A and B, 
        # and the number of edges in the bipartite graph
        m, n, q = [int(x) for x in input().strip().split()]

        # Create the bipartite graph (A will be indices 2 through m + 1, B will be indices m + 2 through m + n + 1)
        graph: dict[int, OptimizedNode] = {}

        # print('A has', m, 'elements')
        # print('B has', n, 'elements')
        # print('We\'ll have', q, 'edges')

        for _ in range(q):
            # Get indices of A and B where the edge will go between
            ai, bi = [int(x) for x in input().strip().split()]
            ai += 1
            bi += m + 1

            # Create A[ai] and B[bi] if they don't already exist
            if graph.get(ai, None) == None:
                graph.update({ai: OptimizedNode(ai)})
            if graph.get(bi, None) == None:
                graph.update({bi: OptimizedNode(bi)})

            # Create the edge going from A[ai] to B[bi]
            e = Edge(graph.get(ai), graph.get(bi), 1)
            graph.get(ai).updateEdge(e)
            # print('Edge between node', ai, 'and', bi)
            # graph.get(bi).links.append(e)

        # Create a faucet node (stored at graph[1]) and connect it to all nodes in A
        faucetIndex = 1
        graph.update({faucetIndex: OptimizedNode(faucetIndex)})
        faucet = graph.get(faucetIndex)
        for i in range(2, m + 2):
            # print('Connecting faucet to node', i)
            node = graph.get(i, None)
            if node == None: continue

            e = Edge(faucet, node, 1)
            faucet.updateEdge(e)
        
        # Create a sink node and connect it to all nodes in B
        sinkIndex = m + n + 2
        graph.update({sinkIndex: OptimizedNode(sinkIndex)})
        sink = graph.get(sinkIndex)
        for i in range(m + 2, m + n + 2):
            # print('Connecting node', i, 'to sink')
            node = graph.get(i, None)
            if node == None: continue

            e = Edge(node, sink, 1)
            node.updateEdge(e)
        
        # Find its max flow and compare it
        mf = OptimizedMaxFlow(graph.get(1), graph.get(m + n + 2), 1)
        perfect = 'Y' if m == n and mf == m else 'N'
        print(str(mf) + ' ' + perfect)