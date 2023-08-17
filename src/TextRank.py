import networkx as nx
from pydantic import BaseModel
from typing import List, Optional

def textrank(corpus: List[list], top_n: Optional[int] = None, remove_stop: Optional[list] = None) -> list:

    G = nx.Graph()

    for c in corpus:
        for i in range(len(c) - 1):
            G.add_edge(c[i], c[i + 1])
    pr = nx.pagerank(G)
    
    if remove_stop != None :
        for stopword in remove_stop:
            try:
                del pr[stopword]
            except:
                pass

    sorted_pr = sorted(pr.items(), key=lambda item: item[1], reverse=True)

    if top_n == None:
        return sorted_pr 
    else:
        return sorted_pr[:top_n]
