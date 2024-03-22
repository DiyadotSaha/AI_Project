# Project for AI

## Introduction
This project focuses on solving the Traveling Salesman Problem (TSP). The TSP is a classic optimization problem in which a salesman seeks to find the shortest route that visits each city exactly once and returns to the original city.

## The Two Approaches
In this project, we explore two approaches to solve the TSP:
1. Stochastic Search: This approach involves exploring a large search space using random or probabilistic methods to find an optimal or near-optimal solution.
2. Heuristic Search: This approach employs simple, rule-based strategies to efficiently find a good solution, often sacrificing optimality for computational efficiency.

## How to Run the Program
To run both the searches you can use the `run_script.py`. An example command to run this file is 
```
python3 run_script.py -n 40 -k 30 -u 10 -v 2
```
This command with run both the local search and the heuristic search with the following parameters 40 locations(n), 30 distinct distance values(k), a mean of 10(u) and a variance of 2(v). 

To generate different TSP instances, you can use the `generate_TSP.py` file. Below is an example command to generate a TSP problem:
  
  ``` python genTSP.py -n 5 -k 3 -u 10 -v 5 -p 3 ```.
This command generates 3 TSP instances with 5 locations, 3 distinct distance values, a mean of 10, a variance of 5 and 3 different TSP problem instances.

After generating TSP instances, you can run the solving algorithm on them. For example, if you have a TSP instance file named `tsp-problem-5-3-10-5-1.txt`, `tsp-problem-5-3-10-5-2.txt` and `tsp-problem-5-3-10-5-3.txt` you can run the solving algorithm using the following command:
