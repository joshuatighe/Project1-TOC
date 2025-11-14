import csv

import matplotlib.pyplot as plt

def parse_results(csv_path):
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        results = []
        for row in csv_reader:
            results.append(row)

    return results

def plot_results(all_results):
    bf_X = [result[6] for result in all_results[0]]
    bf_Y = [result[3] for result in all_results[0]]

    bt_X = [result[6] for result in all_results[1]]
    bt_Y = [result[3] for result in all_results[1]]

    fig, ax = plt.subplots()
    ax.scatter(bf_X, bf_Y, color="red")
    ax.scatter(bt_X, bt_Y, color="green")
    ax.set_title("Size of Problem vs. Execution Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of Colors")
    ax.grid(True)

    plt.savefig('../results/graph_input_graph_coloring_results.png')

bf_results_csv_path = '../results/brute_force_graph_input_graph_coloring_results.csv'
bt_results_csv_path = '../results/btracking_graph_input_graph_coloring_results.csv'

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

all_results = (bf_results, bt_results)

plot_results(all_results)
