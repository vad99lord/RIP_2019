from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor
import math

class Circle(GeometricFigure):

    figure_name = "Круг"

    @classmethod
    def get_fig_name(cls):
        return cls.figure_name

    def __init__(self, color, radius):
        self.radius = radius
        self.fig_col = FigureColor()
        self.fig_col.color = color

    def area(self):
        return self.radius*math.pi

    def __repr__(self):
        return 'фигура: {}, цвет: {}, радиус = {}, площадь = {}.'.format(
            self.get_fig_name(),
            self.fig_col.color,
            self.radius,
            self.area()
        )
