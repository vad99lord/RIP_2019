from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor


class Rectangle(GeometricFigure):

    figure_name = "Прямоугольник"

    @classmethod
    def get_fig_name(cls):
        return cls.figure_name

    def __init__(self, color, width, height):
        self.height = height
        self.width = width
        self.fig_col = FigureColor()
        self.fig_col.color = color

    def area(self):
        return self.height*self.width

    def __repr__(self):
        return 'фигура: {}, цвет: {}, ширина = {}, высота = {} площадь = {}.'.format(
            self.get_fig_name(),
            self.fig_col.color,
            self.width,
            self.height,
            self.area()
        )
