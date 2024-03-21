import os
import subprocess
import argparse
import h_search
import local_search
import time


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

    parser = argparse.ArgumentParser(description="Generate random Traveling Sales Person problems.")
    parser.add_argument("-n", "--n", help="N: number of locations", required=True, type=int)
    parser.add_argument("-k", "--k", help="K: number of distinct distance values to use", required=True, type=int)
    parser.add_argument("-u", "--u", help="U: mean of normal distribution for distances", required=True, type=int)
    parser.add_argument("-v", "--v", help="V: variance of normal distribution for distances", required=True, type=int)
    parser.add_argument("-p", "--p", help="P: number of problem instances to generate (default: 1)", required=False, type=int, default=1)
    args = parser.parse_args()

    n = args.n
    k = args.k
    u = args.u
    v = args.v
    p = args.p
    generate_TSP_instance(n, k, u, v, p)

    filename = f"tsp-problem-{n}-{k}-{u}-{v}-1.txt"
    start = time.process_time()
    result = h_search.nearest_neighbor_tsp(filename)
    print("Time to complete nearest neighbour: {} ms".format((time.process_time() - start)*1000))
    print("Running TSP using heauristic search: Nearest Neighbour---------")
    print("Optimal Path:", result[0])
    print("Total Distance:", result[1])
    print("\n\nRunning TSP using Local search: ---------")
    start = time.process_time()
    result = local_search.run_local_search(filename)
    print("Time to complete 2OPT: {} ms".format((time.process_time() - start)*1000))
    print("Optimal Path:", result[1])
    print("Total Distance:", result[0])

if __name__ == "__main__":
    main()
