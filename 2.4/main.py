import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("График")
        self.root.geometry("600x500")

        self.plot_button = tk.Button(root, text="Построить график y = x^2",
                                     command=self.plot_graph, font=("Arial", 12))
        self.plot_button.pack(pady=10)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def plot_graph(self):
        self.ax.clear()

        x = list(range(11))
        y = [i ** 2 for i in x]

        self.ax.plot(x, y, 'ro-', linewidth=2, markersize=6)
        self.ax.set_title("График y = x^2", fontsize=14)
        self.ax.set_xlabel("X", fontsize=12)
        self.ax.set_ylabel("Y", fontsize=12)
        self.ax.grid(True, alpha=0.3)

        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()