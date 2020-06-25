import sys

from heapq import heappush

class PriorityQueue(object):
  def __init__(self):
    self.queue = []
    
  def add(self, item):
    return heappush(self.queue, item)

  def remove(self):
    return self.queue.pop(0)

  def isEmpty(self):
    return not self.queue    
    

def createGraph(filename):
  try:
    graph = {}                             
    file = open(filename, 'r')
    for line in file:
      if 'END OF INPUT' in line:
        return graph
      line = line.split()
      graph.setdefault(line[0], []).append((line[1], line[2]))
      graph.setdefault(line[1], []).append((line[0], line[2]))
  except:
    print("error occured")

def uniformedCostSearch(graph, start, goal):
  try:
    visited = set()
    path = [] 
    queue = PriorityQueue()
    queue.add((0, [start]))
    while queue:
      if queue.isEmpty():
        print ('distance: infinity')
        print('route:')
        print('none')
        return []
      cost, path = queue.remove()
      last_index = len(path)-1
      node = path[last_index]
      if node not in visited:
        visited.add(node)
        if node == goal:
          path.append(cost) 
          return path
        neighbors_of_node = neighbors(graph, node)
        for x in neighbors_of_node:
          if x not in visited:
            total_cost = cost + int(getCost(graph, node, x))
            temporary = path[:]
            temporary.append(x)
            queue.add((total_cost, temporary)) 
  except:
    print("error occured 3")
    return []

def neighbors(graph,node):
  elements = graph[node]
  neighbors = []
  for x in elements:
    neighbors.append(x[0])
  return neighbors

def getCost(graph, from_node, to_node):
  try: 
    position = []
    for x in graph[from_node]:
      position.append(x[0])
    index = position.index(to_node)
    return graph[from_node][index][1]
  except:
    print("error occured")

def displayPath(graph,path):
  distance = path[-1]
  print ('distance: %s' % (distance))
  print ('route: ')
  for x in path[:-2]:
    try:
      y = path.index(x)
      position = []
      for z in graph[x]:
        position.append(z[0])
      index = position.index(path[y+1])
      cost = graph[x][index][1]
      print ('%s %s %s' % (x,path[y+1],cost))
    except:
    	print("error occured 1")


if __name__ == '__main__':
  (filename, start, goal) = (sys.argv[1], sys.argv[2], sys.argv[3])

  graph = createGraph(filename)

  if start not in graph.keys() or goal not in graph.keys():
    print ('Improper start or goal node')
    sys.exit()
  path = []
  path = uniformedCostSearch(graph, start, goal)
  
  if len(path) > 0:
    displayPath(graph,path)

 
