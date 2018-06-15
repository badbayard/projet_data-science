import networkx as nx
import os 
import seaborn as sns
import matplotlib.pyplot as plt
#from networkx.drawing.nx_agraph import graphviz_layout

def start_graph(Nomserie,type_graph) :
    print(type_graph)
    options = {
         'node_color': 'red',
         'node_size': 200,
         'width': 3,
         }
    
    if Nomserie == "Game of Thrones":
        G1=nx.read_graphml("data/got/GoT_S05E09_1039.graphml")
        print(G1)
    if Nomserie ==  "Breaking Bad":
        G1=nx.read_graphml("data/bb/BB_S03E11_598.graphml")
    if Nomserie == "House of Card":
        G1=nx.read_graphml("data/hoc/HoC_S02E13_879.graphml")
        
    G1.remove_nodes_from(nx.isolates(G1))
    if type_graph == "Classical":
        nx.draw_networkx(G1,pos=nx.spring_layout(G1))
    if type_graph ==  "Random":
        nx.draw_random(G1,**options,with_labels=True,font_weight='bold')
    if type_graph == "Circular":
        nx.draw_circular(G1,**options,with_labels=True,font_weight='bold')
    if type_graph == "Spectral":
        nx.draw_spectral(G1,**options,with_labels=True,font_weight='bold')
    if type_graph == "Shell":
        nx.draw_shell(G1,**options,with_labels=True,font_weight='bold')
    plt.savefig("images/" + Nomserie+"_"+type_graph+ ".jpg")
    plt.close('all')
    