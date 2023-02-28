import src.Graph as Graph

def DFSUtil(Graph, v, visited):
    # Mark the current node as visited
    # and print it
    visited.add(v)
    print(v, end=' ')

    # Recur for all the vertices
    # adjacent to this vertex
    for neighbour in Graph.graph[v]:
        if neighbour not in visited:
            DFSUtil(Graph, neighbour, visited)
 
# The function to do DFS traversal. It uses
# recursive DFSUtil()
def DFS(g, v):
    # Create a set to store visited vertices
    visited = set()
    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(g, v, visited)