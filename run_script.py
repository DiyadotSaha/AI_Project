import os
import subprocess
import h_search

def generate_TSP_instance(n, k, u, v, p):
    genTSP_command = f"python3 generate_TSP.py -n {n} -k {k} -u {u} -v {v} -p {p}"
    subprocess.run(genTSP_command, shell=True)

def run_h_search(filename):
    h_search_command = f"python3 h_search.py {filename}"
    result = subprocess.run(h_search_command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    # Parameters for generating TSP instance
    n = 5  
    k = 3  
    u = 10  
    v = 5   
    p = 1   

    generate_TSP_instance(n, k, u, v, p)

    filename = f"tsp-problem-{n}-{k}-{u}-{v}-1.txt"
    result = h_search.nearest_neighbor_tsp(filename)
    
    print("Optimal Path:", result[0])
    print("Total Distance:", result[1])

if __name__ == "__main__":
    main()
