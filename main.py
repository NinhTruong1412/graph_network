from src import Graph, BFS, DFS
import matplotlib.pyplot as plt



      
if __name__ == '__main__':
    # # g = Graph()
    # # # Add each edges to graph
    # # g.add_edge('a', 'b', 7)  
    # # g.add_edge('a', 'c', 9)
    # # g.add_edge('a', 'f', 14)
    # # g.add_edge('b', 'c', 10)
    # # g.add_edge('b', 'd', 15)
    # # g.add_edge('c', 'd', 11)
    # # g.add_edge('c', 'f', 2)
    # # g.add_edge('d', 'e', 6)
    # # g.add_edge('e', 'f', 9)
    # # g.visualize(True)

    # # Add list of edges
    # word_transform_edges = [
    #     ("FOOD", "FOOT"),
    #     ("FOOD", "GOOD"),
    #     ("FOOD", "FOOL"),
    #     ("FOOT", "FORT"),
    #     ("FOOT", "FOOD"),
    #     ("FORT", "FOOT"),
    #     ("GOOD", "FOOD"),
    #     ("FOOL", "FOOD"),
    #     ("FOOL", "POOL"),
    #     ("POOL", "POLL"),
    #     ("POOL", "FOOL"),
    #     ("POLL", "POLE"),
    #     ("POLL", "POOL"),
    #     ("POLE", "POLL"),
    #     ("POLE", "PALE"),
    #     ("PALE", "SALE"),
    #     ("PALE", "POLE"),
    #     ("PALE", "SAGE"),
    #     ("PALE", "PALM"),
    #     ("PALM", "PALE"),
    #     ("SALE", "PALE"),
    #     ("SAGE", "SALT"),
    #     ("SAGE", "PALE"),
    #     ("SALT", "SAGE"),
    # ]
    # g = Graph()
    # g.add_list_edges(word_transform_edges)
    # g.visualize(False)
    # for v in g:
    #     for w in v.get_connections():
    #         print("( %s , %s )" % (v.get_id(), w.get_id()))
    # g.BFS("FOOD")

    # plt.show()

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    BFS(g, 2)

    print("\nFollowing is Depth First Traversal"
        " (starting from vertex 2)")
    DFS(g, 2)
    # g.visualize(False)
    # plt.show()