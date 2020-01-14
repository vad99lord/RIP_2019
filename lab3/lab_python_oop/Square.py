from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.FigureColor import FigureColor


class Square(Rectangle):

    figure_name = "Квадрат"

    @classmethod
    def get_fig_name(cls):
        return cls.figure_name

    def __init__(self, color, length):
        super().__init__(color, length, length)
        self.length = length
        self.fig_col = FigureColor()
        self.fig_col.color = color

    def __repr__(self):
        return 'фигура: {}, цвет: {}, сторона = {} площадь = {}.'.format(
            self.get_fig_name(),
            self.fig_col.color,
            self.length,
            self.area()
        )