import argparse
import numpy as np

class City:
    x = 0
    def __init__(self, x):
        self.x = x

def distance(city1, city2, graph):
    return graph[city1.x][city2.x]

def path_cost(path, graph):
    cost = 0
    for i in range(len(path)):
        cost += distance(path[i], path[(i+1)%len(path)], graph)

    return cost

def genGraph(filename):
    with open(filename, "r") as file:
        num_nodes = int(file.readline().strip())
        # Read the adjacency matrix
        graph = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            row = list(map(float, file.readline().strip().split()))
            graph[i] = row
        return graph

def genInitialPath(graph):
    path = []
    for i in range(len(graph)):
        path.append(City(i))
    path.append(City(0))    
    return path

def two_opt_swap(path, graph, i, j):
    # for k in range(len(path)):
    #     print(path[k].x, end=' ')
    new_path = path[:i+1]
    new_path.extend(reversed(path[i+1:j+1]))
    new_path.extend(path[j+1:])
    # print('new path : ', len(new_path))
    # print('i :', i, ' j :', j)
    # for i in range(len(new_path)):
    #     print(new_path[i].x, end=' ')
    return new_path

if __name__ == "__main__":

    # parse parameters
    parser = argparse.ArgumentParser(description="Generate graph for local serach.")
    parser.add_argument("-f", "--f", help="file name: to generate graph from", required=True, type=str)
   
    args = parser.parse_args()

    filename = args.f
    graph = genGraph(filename).tolist()
    n = len(graph)
    path = genInitialPath(graph)

    currCost = path_cost(path, graph)
    print("Initial Path cost:", currCost)
    isImproved = True
    count = 0
    while isImproved and count < 1000:
        isImproved = False
        for i in range(0, n-1):
            for j in range(i+1, n):
                
                costDiff = distance(path[i], path[j], graph) + distance(path[i+1], path[(j+1)%n], graph) - distance(path[i], path[i+1], graph) - distance(path[j], path[(j+1)%n], graph)
                # print('distance(path[i], path[j], graph) : ' , distance(path[i], path[j], graph))
                # print('distance(path[i+1], path[(j+1)%n], graph) : ' , distance(path[i+1], path[(j+1)%n], graph))
                # print('distance(path[i], path[i+1], graph) : ' , distance(path[i], path[i+1], graph))
                # print('distance(path[j], path[(j+1)%n], graph) : ' , distance(path[j], path[(j+1)%n], graph))
                if costDiff < 0:
                    print('yes')
                    print('costDiff : ', costDiff)  
                    path = two_opt_swap(path, graph, i, j)
                    print('currCost before : ', currCost) 
                    currCost += costDiff
                    print('currCost : ', currCost) 
                    isImproved = True
        count+=1
        print('count : ' , count)
        #print('currCost : ', currCost)    
    print('best cost : ', currCost)
    for i in range(len(path)):
        print(path[i].x, end=' ')
    #print(path)                
    