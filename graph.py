graph = {}

def add_node(val):
	lst = []
	for i in range(val):
		node = int(input("Add the node - "))
		lst.append(node)
	for i in lst:
		graph[i]=[]

def add_edge(edg):
	n = int(input("No. of edges you want to add - "))
	ls=[]
	for i in range(n):
		e = int(input("connected edge - "))
		ls.append(e)
	graph[edg].append(ls)

def rem_node(nod_to_rem):
	for i,j in graph:
		

nod = int(input("No of nodes you want to add - "))
add_node(nod)
e = int(input("to which node you want to add the edge to- "))
add_edge(e)
print(graph)