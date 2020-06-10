import matplotlib.pyplot as plt
from matplotlib.patches import *
from deprecated.new_new_old.Configuration import Configuration as cfg


from deprecated.new_old.Enums import State


class Drawer:  # class responsible for drawing current iteration on matplotlib plot

    @staticmethod
    def draw_from_grid_WIP(grid, society):
        hex_size = cfg.get('hex_size')
        fig, ax = plt.subplots()
        xmax = 0
        xmin = 0
        ymax = 0
        ymin = 0
        grid_listed = grid.get_grid_in_cartesian()
        for x, y, value in grid_listed:
            xmax = max(xmax, x)
            xmin = min(xmin, x)
            ymax = max(ymax, y)
            ymin = min(ymin, y)
            if society.get_being(value['person']).state == State.Inactive:
                hexes = RegularPolygon((x, y), numVertices=6, radius=hex_size, alpha=1, edgecolor='k', facecolor='w')
                ax.add_patch(hexes)
            elif society.get_being(value['person']).state == State.Susceptible:
                hexes = RegularPolygon((x, y), numVertices=6, radius=hex_size, alpha=1, edgecolor='k', facecolor='b')
                ax.add_patch(hexes)
            elif society.get_being(value['person']).state == State.Infectious:
                hexes = RegularPolygon((x, y), numVertices=6, radius=hex_size, alpha=1, edgecolor='k', facecolor='r')
                ax.add_patch(hexes)
            elif society.get_being(value['person']).state == State.Deceased:
                hexes = RegularPolygon((x, y), numVertices=6, radius=hex_size, alpha=1,
                                       edgecolor='k', facecolor='0.5')
                ax.add_patch(hexes)
            elif society.get_being(value['person']).state == State.Recovered:
                hexes = RegularPolygon((x, y), numVertices=6, radius=hex_size, alpha=1, edgecolor='k', facecolor='g')
                ax.add_patch(hexes)
        plot_border = 10
        ax.set_xlim([xmin - plot_border, xmax + plot_border])
        ax.set_ylim([ymin - plot_border, ymax + plot_border])
        plt.grid(False)
        plt.axis('off')
        susceptible = Patch(color='b', label='Susceptible')
        infectious = Patch(color='r', label='Infectious')
        deceased = Patch(color='0.5', label='Deceased')
        recovered = Patch(color='g', label='Recovered')
        plt.legend(handles=[susceptible, infectious, deceased, recovered])
        plt.show()

        # def draw_hexes(self, hexagons, population):
        #     fig, ax = plt.subplots()
        #     xmax = 0
        #     xmin = 0
        #     ymax = 0
        #     ymin = 0
        #     for hexagon in hexagons:
        #         x, y = hexagon.get_cartesian_coordinates()
        #         xmax = max(xmax, x)
        #         xmin = min(xmin, x)
        #         ymax = max(ymax, y)
        #         ymin = min(ymin, y)
        #         hexes = RegularPolygon((x, y), numVertices=6, radius=hexagon.size, alpha=1, edgecolor='k', facecolor='w')
        #         ax.add_patch(hexes)
        #     for person in population:
        #         x, y = person.get_cartesian_coordinates()
        #         if person.state == State.Susceptible:
        #             hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='b')
        #             ax.add_patch(hexes)
        #         elif person.state == State.Infectious:
        #             hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='r')
        #             ax.add_patch(hexes)
        #         elif person.state == State.Deceased:
        #             hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1,
        #                                    edgecolor='k', facecolor='0.5')
        #             ax.add_patch(hexes)
        #         elif person.state == State.Recovered:
        #             hexes = RegularPolygon((x, y), numVertices=6, radius=person.size, alpha=1, edgecolor='k', facecolor='g')
        #             ax.add_patch(hexes)
        #     plot_border = 10
        #     ax.set_xlim([xmin-plot_border, xmax+plot_border])
        #     ax.set_ylim([ymin-plot_border, ymax+plot_border])
        #     plt.grid(False)
        #     plt.axis('off')
        #     susceptible = Patch(color='b', label='Susceptible')
        #     infectious = Patch(color='r', label='Infectious')
        #     deceased = Patch(color='0.5', label='Deceased')
        #     recovered = Patch(color='g', label='Recovered')
        #     plt.legend(handles=[susceptible, infectious, deceased, recovered])
        #     plt.show()