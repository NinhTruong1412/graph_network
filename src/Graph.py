import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import src.Vertex as Vertex

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vert_dict = {}
        self.num_vertices = 0
        self.visual = []
        self.weight = []

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    def add_list_edges(self, edges: list):
        """Add edges to graph

        Args:
            edges (list): List of edges
        """
        for node1, node2 in edges:
            self.add_edge(node1, node2)
        


    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
        temp = [frm, to]
        self.visual.append(temp)
        temp2 = (frm, to, cost)
        self.weight.append(temp2)
        self.graph[frm].append(to)

    def get_vertices(self):
        return self.vert_dict.keys()

    def visualize(self, weight = False):
      G = nx.Graph()
      if weight == False:
        G.add_edges_from(self.visual)
        fig, ax = plt.subplots(figsize=(10,10))
        nx.draw_networkx(G, ax = ax)
      else:
        # G.add_edges_from(self.visual)
        G.add_weighted_edges_from(self.weight)
        pos = nx.spring_layout(G, dim = 2) 
        # nx.draw_networkx(G)
        # Nodes
        fig, ax = plt.subplots(figsize=(10,10))
        nx.draw_networkx_nodes(G, pos, ax = ax)
        # edges
        nx.draw_networkx_edges(G, pos, width=1, ax = ax)
        nx.draw_networkx_edges(
            G, pos, width=0.2, alpha=0.5, edge_color="b", style="dashed", ax = ax
        )
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif", ax = ax)
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, ax = ax)
    
    