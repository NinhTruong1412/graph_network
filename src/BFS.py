import src.Graph as Graph



# Function to print a BFS of graph
def BFS(Graph, s):
    # Mark all the vertices as not visited
    visited = [False] * (max(Graph.graph) + 1)

    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        print(s, end=" ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in Graph.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True