#
# Kruskals Algorithm
#
# Input in the format of:
#
# number of vertices, n
# number of edges, m
# graph(vertex_1, vertex_2, edge_weight):
#
#
# Example:
# 2
# 1
# 1 2 6

n = input()
m = input()

edges = []
vertices = []

while True:
	try:
		line = input().split()

		temp = line[2], line[0], line[1]

		if temp[1] not in vertices and temp[2] not in vertices:
			vertices.append(temp[1])
			vertices.append(temp[2])

		edges.append(temp)
	except(EOFError):
		break


# Kruskal's Algorithm
invariant = dict()
rank = dict()

def kruskals_algorithm(edges, vertices):
	mst = []
	for vertex in vertices:
		make(vertex)

	edges.sort()
	for e in edges:
		w, v1, v2 = e

		# If they share different invariants, there is no cycle
		if find(v1) != find(v2):
			union(v1, v2)
			mst.append(e)
	return mst


# Union-Find Data Structure
# Lazy unions by rank with path compression
def make(v):
	invariant[v] = v
	rank[v] = 0

def find(v):
	if invariant[v] != v:
		# Path compression
		invariant[v] = find(invariant[v])
	return invariant[v]

def union(v1, v2):
	rootA = find(v1)
	rootB = find(v2)

	if rank[rootA] > rank[rootB]:
		invariant[rootB] = rootA
	else:
		invariant[rootA] = rootB
		if rank[rootA] == rank[rootB]:
			rank[rootB] += 1

print(kruskals_algorithm(edges, vertices))
