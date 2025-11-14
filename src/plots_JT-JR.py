import csv

import matplotlib.pyplot as plt

def parse_results(csv_path):
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # skip title row

        results = []
        for row in csv_reader:
            results.append(row)

    return results

def plot_results(results, output_path, log=False):
    solution_X = [float(result[6]) for result in results if result[5] == "YES"]
    soltion_Y = [int(result[1]) for result in results if result[5] == "YES"]

    no_solution_X = [float(result[6]) for result in results if result[5] == "NO"]
    no_solution_Y = [int(result[1]) for result in results if result[5] == "NO"]

    plt.scatter(solution_X, soltion_Y, color="green", label="Colorable")
    plt.scatter(no_solution_X, no_solution_Y, color="red", label="Not Colorable")

    if log: plt.xscale("log")

    plt.title("# Vertices vs. Time")
    plt.xlabel("Time")
    plt.ylabel("# Vertices")

    plt.legend()

    plt.savefig(output_path)

    plt.clf()

bf_results_csv_path = '../results/brute_force_graph_input_JT-JR_graph_coloring_results.csv'
bt_results_csv_path = '../results/btracking_graph_input_JT-JR_graph_coloring_results.csv'

# results indices
# 0 -> instance_id
# 1 -> n_vertices
# 2 -> n_edges
# 3 -> k
# 4 -> method
# 5 -> colorable
# 6 -> time_seconds
# 7 -> coloring
bf_results = parse_results(bf_results_csv_path)
bt_results = parse_results(bt_results_csv_path)

plot_results(bf_results, '../results/graph_input_graph_coloring_results_bf_JT-JR.png', log=True)
plot_results(bt_results, '../results/graph_input_graph_coloring_results_bt_JT-JR.png')
