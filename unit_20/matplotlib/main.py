import heapq

def dijkstra(adj, costs, s, t):
    ''' Return predecessors and min distance if there exists a shortest path 
        from s to t; Otherwise, return None '''
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
#         print(Q)
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
#             print('visit:', u)
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost
# adjacent list
adj = { 1: [2, 3, 5, 7],
        2: [1, 4],
        3: [1, 5, 6,7],
        4: [2, 5, 7],
        5: [1, 3, 4, 6],
        6: [3, 5],
        7: [1, 3, 4]}
    
# edge costs
edges = {(1, 2): 4, (4, 7): 3, (1, 3): 6, (4, 5): 15,
        (1, 5): 7, (1, 6): 6, (3, 6): 5, (1, 7): 15, 
        (5, 6): 5, (3, 7): 5, (2, 4): 10, (3, 5): 10}

edge_cost = make_undirected(edges)

source, target = 1, 7
predecessors, min_cost = dijkstra(adj, edge_cost, source, target)
c = target
path = [c]
print('Minimal cost from {0} to {1}: {2}'.format(source, target, min_cost))
while predecessors.get(c):
    path.insert(0, predecessors[c])
    c = predecessors[c]

print('shortest path from {0} to {1}: {2}'.format(source, target, path))
