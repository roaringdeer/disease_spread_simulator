import matplotlib.pyplot as plt
from matplotlib.patches import *
import numpy as np

from Enums import State


class Drawer:

    def __init__(self):
        pass

    def draw_hexes(self, hexagons, population):
        fig, ax = plt.subplots()
        xmax = 0
        xmin = 0
        ymax = 0
        ymin = 0
        for hexagon in hexagons:
            x, y = hexagon.get_cartesian_coordinates()
            xmax = max(xmax, x)
            xmin = min(xmin, x)
            ymax = max(ymax, y)
            ymin = min(ymin, y)
            hexes = RegularPolygon((x, y), numVertices=6, radius=hexagon.size, alpha=1, edgecolor='k', facecolor='w')
            ax.add_patch(hexes)
        for person in population:
            x, y = person.get_cartesian_coordinates()
            if person.state == State.Susceptible:
                hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='b')
                ax.add_patch(hexes)
            elif person.state == State.Infectious:
                hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='r')
                ax.add_patch(hexes)
            elif person.state == State.Deceased:
                hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1,
                                       edgecolor='k', facecolor='0.5')
                ax.add_patch(hexes)
            elif person.state == State.Recovered:
                hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='g')
                ax.add_patch(hexes)
        plot_border = 10
        ax.set_xlim([xmin-plot_border, xmax+plot_border])
        ax.set_ylim([ymin-plot_border, ymax+plot_border])
        plt.grid(False)
        plt.axis('off')
        susceptible = Patch(color='b', label='Susceptible')
        infectious = Patch(color='r', label='Infectious')
        deceased = Patch(color='0.5', label='Deceased')
        recovered = Patch(color='g', label='Recovered')
        plt.legend(handles=[susceptible, infectious, deceased, recovered])
        plt.show()
