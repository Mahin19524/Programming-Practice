import tkinter as tk
import random

class GraphVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("DFS Visualizer")
        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.nodes = {}
        self.edges = []

        # Create buttons
        self.generate_button = tk.Button(self.master, text="Generate Graph", command=self.generate_graph)
        self.generate_button.pack(side=tk.LEFT, padx=10)
        self.dfs_button = tk.Button(self.master, text="Run DFS", command=self.run_dfs)
        self.dfs_button.pack(side=tk.LEFT, padx=10)

    def generate_graph(self):
        # Clear previous graph
        self.canvas.delete("all")
        self.nodes = {}
        self.edges = []

        # Generate random nodes
        for i in range(5):
            x = random.randint(50, 550)
            y = random.randint(50, 350)
            node_id = f"node_{i}"
            self.nodes[node_id] = (x, y)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.canvas.create_text(x, y - 15, text=node_id)

        # Generate random edges
        for i in range(random.randint(5, 10)):
            start_node = random.choice(list(self.nodes.keys()))
            end_node = random.choice(list(self.nodes.keys()))
            if start_node != end_node and (start_node, end_node) not in self.edges:
                self.edges.append((start_node, end_node))
                x1, y1 = self.nodes[start_node]
                x2, y2 = self.nodes[end_node]
                self.canvas.create_line(x1, y1, x2, y2, fill="black")

    def run_dfs(self):
        # Perform Depth-First Search
        visited = set()
        start_node = random.choice(list(self.nodes.keys()))
        self.dfs(start_node, visited)

    def dfs(self, node, visited):
        if node not in visited:
            visited.add(node)
            self.canvas.itemconfig(node, fill="red")  # Highlight visited node
            self.master.update()
            self.master.after(500)  # Delay for visualization
            for neighbor in self.get_neighbors(node):
                self.dfs(neighbor, visited)

    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge[0] == node:
                neighbors.append(edge[1])
        return neighbors

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualizer(root)
    root.mainloop()
