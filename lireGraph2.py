import networkx as nx
import os 
import seaborn as sns
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


tableau_closeness_centrality = []
tableau_degree_centrality = []
tableau_pagerank = []
tableau_betweeness = []
dicoNomToNum = dict()
numNoeud = ""


def type_centralite_voulu(numNoeud, operations) :
    
    liste = operations
    i = 0
    tab =[]

    if 'd' in liste:
        tab.append([x[numNoeud] for x in tableau_degree_centrality])
        sns.tsplot(tab[i], color = "blue")
        i+=1
    if 'c' in liste:
        tab.append([x[numNoeud] for x in tableau_closeness_centrality])
        sns.tsplot(tab[i], color = "red")
        i+=1
    if 'p' in liste:
        tab.append([x[numNoeud] for x in tableau_pagerank])
        sns.tsplot(tab[i], color = "black")
        i+=1
    if 'b' in liste:
        tab.append([x[numNoeud] for x in tableau_betweeness])
        sns.tsplot(tab[i], color = "green")
        i+=1


def recherche_nom(nom, operations) :
    nomNoeud = str(nom)
    numNoeud = dicoNomToNum[nomNoeud]
    
    type_centralite_voulu(numNoeud, operations)
    
    plt.savefig("images/" + nom + operations + ".jpg")
    
    plt.clf()
    plt.close('all')


def start_main(Nomserie,nbScenes, nom, operations) :

    if Nomserie == "Game of Thrones":
        """ On crée un dictionnaire qui associe les noms des persos à leur numéro de noeud """
        G1=nx.read_graphml("data/got/GoT_S05E09_1039.graphml")
        serie ="got"
    if Nomserie ==  "Breaking Bad":
        G1=nx.read_graphml("data/bb/BB_S03E11_598.graphml")
        serie = "bb"
    if Nomserie == "House of Card":
        G1=nx.read_graphml("data/hoc/HoC_S02E13_879.graphml")
        serie = "hoc"
    dicoNumToNom = nx.get_node_attributes(G1,"label")
    for cle in dicoNumToNom : 
        dicoNomToNum[dicoNumToNom[cle]] = cle
        
        
    plage = nbScenes
    if plage > 1039 :
        plage = 1039
    liste_graph = []
    for element in os.listdir('data/'+serie+'/' )[:plage]:
        liste_graph.append(nx.read_graphml("data\\"+serie+"\\"+ str(element)))
            
   
    for l in liste_graph :
        """ |== >  Affichage du graphe de la case liste_graph(l)"""
        tableau_degree_centrality.append(nx.degree_centrality(l))  # une façon de lire la centralité
        tableau_closeness_centrality.append(nx.closeness_centrality(l))
        tableau_pagerank.append(nx.pagerank(l))
        tableau_betweeness.append(nx.betweenness_centrality(l))
            
    recherche_nom(nom, operations)



