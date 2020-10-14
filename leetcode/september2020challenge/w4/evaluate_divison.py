class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class Graph:
            def __init__(self, equations, values):
                self.graph = dict()
                for i in range(len(equations)):
                    tpl = equations[i]
                    cost = values[i]
                    
                    self.addEdge(tpl[0], tpl[1], cost)
            
            def addEdge(self, u, v, cost):
                if u in self.graph:
                    self.graph[u][v] = cost
                else:
                    self.graph[u] = dict()
                    self.graph[u][v] = cost
                    
                if v in self.graph:
                    self.graph[v][u] = 1.0 / cost
                else:
                    self.graph[v] = dict()
                    self.graph[v][u] = 1.0 / cost
            
            def get(self, key):
                return self.graph[key]
            
            def search(self, u, dest, cost, visited):
                visited[u] = True

                if dest in self.graph[u]:
                    return cost * self.graph[u][dest]
                
                else:
                    res = []
                    for key in self.graph[u]:
                        u_key_cost = self.graph[u][key]

                        if visited[key] == False:
                            new_cost = cost * u_key_cost
                            res.append(self.search(key, dest, new_cost, visited))
                    
                    if len(res) == 0:
                        return - 1
                    
                    return max(res)

                return -1
            
            def getCost(self, src, dest):
                if (src in self.graph) and (dest in self.graph):
                    visited = dict()
                    
                    for key in self.graph.keys():
                        visited[key] = False
                    
                    cost = self.search(src, dest, 1, visited)
                    return cost
                else:
                    return -1
                
        # MAIN PROGRAM
        costs = []
        my_graph = Graph(equations, values)
        print(my_graph.graph)
        
        for query in queries:
            costs.append(my_graph.getCost(query[0], query[1]))
            
        return costs