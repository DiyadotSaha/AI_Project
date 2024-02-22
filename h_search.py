import numpy as np
import argparse

def nearest_neighbor(graph, start=0):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    path = [start]
    visited[start] = True
    
    for _ in range(num_nodes - 1):
        current_node = path[-1]
        nearest_neighbor = None
        min_distance = float('inf')
        
        for next_node in range(num_nodes):
            if not visited[next_node] and graph[current_node][next_node] < min_distance:
                nearest_neighbor = next_node
                min_distance = graph[current_node][next_node]
        
        path.append(nearest_neighbor)
        visited[nearest_neighbor] = True
    
    return path

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path)):
        total_distance += graph[path[i-1]][path[i]]
    return total_distance

def main(filename):
    with open(filename, "r") as file:
        num_nodes = int(file.readline().strip())
        # Read the adjacency matrix
        graph = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            row = list(map(float, file.readline().strip().split()))
            graph[i] = row

    start_node = 0
    optimal_path = nearest_neighbor(graph, start_node)
    optimal_path.append(start_node)  # Complete the loop
    total_distance = calculate_total_distance(optimal_path, graph)
    print("Optimal Path:", optimal_path)
    print("Total Distance:", total_distance)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run nearest neighbor algorithm on a TSP instance.")
    parser.add_argument("filename", help="Path to the TSP instance file")
    args = parser.parse_args()
    main(args.filename)