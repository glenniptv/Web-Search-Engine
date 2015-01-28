def link_graph_read_me():
	print """
		Link graph describes inlinks and outlinks as followsL
		{	url1:	[u2, u3, u4.... ],
			url2:   [u1, u3, u4....],
		}
		"""

#Add to graph
def add_to_graph(graph, page, link):
	if page in graph:
		graph[page].append(link)
	else:
		graph[page] = [link]

#Testing procedure
graph = {}

for x in range(1, 10):
	for y in range(1, 10):
		add_to_graph(graph, x, (x+y)/2)

print graph

