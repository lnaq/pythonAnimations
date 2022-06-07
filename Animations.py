from util.config_ops import digest_config

from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.pyplot as plt
from itertools import count
from typing import Sequence

# TODO REMOVE get_x_axis func and impmement it into the constructor
class LineGraph:
    CONFIG = {
        'x_axis': [],
        'y_axis': [],
        'x_range': [],
        'y_range': [],
        'color': 'Red',
        'linewidth': 1,
        'x_val': count(0, 1),
        'interval': 40,
        'figsize': (15,5),
        'title': None,
        'xlabel': None,
        'ylabel': None,
        'plot_style': 'default',
    }

    def __init__(
        self,
        x_range: Sequence[float] = None,
        y_range: Sequence[float] = None,
        **kwargs
    ):
        digest_config(self, kwargs)
        super().__init__(**kwargs)

        if x_range is not None:
            self.x_range[:len(x_range)] = x_range

        if y_range is not None:
            self.y_range[:len(y_range)] = y_range

    def __str__(self) -> str:
        return self.__class__.__name__

    def make_plot(self):
        '''
            This function creates a plot witch
            afterwards will get modified to
            it's defualt values or the inputed
            values.
        '''
        # Plot Style
        plt.style.use(self.plot_style)
        # Plot Fix & Axes
        self.fig, self.axes = plt.subplots(figsize=self.figsize)
        # Plot X & Y Labels
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        # Plot Title
        plt.title(self.title)

    def run(self):
        '''
            This functions creates a plot,
            modefies it and afterwateds
            animates it.
        '''
        # Create Plot
        self.make_plot()
        # Make Animations/Plot
        anim = FuncAnimation(self.fig, self.animate, interval=self.interval)
        # Show plot
        plt.show()

    def get_x_axis(self, i):
        '''
            This function determines whether
            an x axis had been passed on.
            If not than it will create one.
        '''
        if len(self.x_range) == 0:
            self.x_axis.append(next(self.x_val))
        else:
            self.x_axis.append((self.x_range[i]))

    def animate(self, i):
        '''
            This function makes the animation,
            it also loops trough the data in
            order for it to get all the data
            and "animate", the graph.
        '''
        self.get_x_axis(i)
        self.y_axis.append((self.y_range[i]))

        self.axes.plot(
                       self.x_axis, self.y_axis,
                       color=self.color, linewidth=self.linewidth)

    def set_title(self, title: str) -> None:
        self.title = title

    def set_x_label(self, label: str) -> None:
        self.xlabel = label

    def set_y_label(self, label: str) -> None:
        self.ylabel = label

    def set_color(self, color: str) -> None:
        self.color = color

    def set_plot_style(self, style: str) -> None:
        self.plot_style = style

    def set_interval(self, interval: int) -> None:
        self.interval = interval

    def set_figsize(self, figsize: tuple) -> None:
        self.figsize = figsize
