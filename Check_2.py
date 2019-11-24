import networkx as nx
from modularity_maximization import partition
import scipy
from modularity_maximization.utils import get_modularity
karate = nx.read_gml('homework.gml')
G2 = nx.DiGraph(karate)

comm_dict = partition(G2)

print(nx.info(karate))

print('-----------------------------------------------')


G2 = nx.DiGraph(karate)

comm_dict = partition(G2)

print("Community %d"%comm)
print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))
print('Modularity of such partition for karate is %.3f' % get_modularity(karate, comm_dict))