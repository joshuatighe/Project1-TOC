from src.helpers.constants import INPUT_FILE
from src.graph_coloring import GraphColoring 
import matplotlib as plt

def plot(results):

    xGreen = []
    yGreen = [] 
    xRed = []
    yRed = []

    for result in results:

        if result[5] == "NO":
            xRed.append(result[1])
            yRed.append(float(result[6]))
        else:
            xGreen.append(result[1])
            yGreen.append(float(result[6]))

    plt.scatter(xRed, yRed, color="red")
    plt.scatter(xGreen, yGreen, color="green")

    plt.title("Size of Problem vs. Execution Time")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot()
