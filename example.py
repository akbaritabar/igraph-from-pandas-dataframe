from igraph_from_pandas import igraph_from_pandas
import pandas as pd
import igraph as ig
# ============================
#### pandas tables of vertices and edges ####
# ============================
vertices_table = pd.read_csv('sample_data/vertices_table.csv')
edges_table = pd.read_csv('sample_data/edges_table.csv')

# ============================
#### build igraph graph from pandas tables ####
# ============================
relations_graph = igraph_from_pandas(edges_table=edges_table, vertices_table=vertices_table, source_cl='start', target_cl='end', vertex_attrs=list(vertices_table.columns), vertex_id_cl='name', directed=True)

# ============================
#### see graph properties ####
# ============================
print(relations_graph.summary())
relations_graph.vs['name']
relations_graph.vs['age']
relations_graph.vs['gender']
relations_graph.vs['education']

# ============================
#### plot ####
# ============================
layout = relations_graph.layout("fr")
visual_style = dict()
visual_style["vertex_size"] = 10
visual_style["vertex_label_size"] = 15
visual_style["vertex_label_dist"] = 2
# visual_style["edge_label_size"] = 10
# visual_style["edge_label_color"] = "red"
visual_style["vertex_color"] = "red"
visual_style["vertex_label_color"] = "blue"
visual_style["vertex_label"] = relations_graph.vs["name"]
visual_style["edge_width"] = 1
visual_style["layout"] = layout
visual_style["margin"] = 100
ig.plot(relations_graph, **visual_style)
