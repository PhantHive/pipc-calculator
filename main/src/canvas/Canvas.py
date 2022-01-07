from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


def dark_style():
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey
    plt.rcParams["axes.edgecolor"] = "white"
    plt.rcParams["axes.linewidth"] = 1


class Canvas(FigureCanvas):

    def __init__(self, parent):
        dark_style()

        fig, self.ax = plt.subplots(dpi=77)
        super().__init__(fig)
        self.setParent(parent)
        self.ax.grid(c="#003740")

    def plot(self, x, y):
        self.ax.clear()
        self.ax.set(xlabel='Nombre d\'itération', ylabel='Temps d\'execution (ms)', title='Temps d\'execution en '
                                                                                          'fonction du nombre '
                                                                                          'd\'itération')
        self.ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
        self.ax.grid(c="#003740")
        self.ax.plot(x, y)
