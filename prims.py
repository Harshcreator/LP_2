import heapq

def prims_algorithm(graph, start_node):
    """
    Implements Prim's Algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    :param graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    :param start_node: The starting node for the algorithm.
    :return: A list of edges in the MST and the total weight of the MST.
    """
    mst = []  # List to store the edges of the Minimum Spanning Tree
    visited = set()  # Set to track visited nodes
    min_heap = [(0, start_node, None)]  # Min-heap to prioritize edges by weight (weight, current_node, parent_node)
    total_weight = 0

    while min_heap:
        weight, current_node, parent_node = heapq.heappop(min_heap)

        if current_node not in visited:
            visited.add(current_node)
            total_weight += weight

            if parent_node is not None:
                mst.append((parent_node, current_node, weight))

            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst, total_weight

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }
    start_node = 'A'
    mst, total_weight = prims_algorithm(graph, start_node)
    print("Minimum Spanning Tree:", mst)
    print("Total Weight:", total_weight)