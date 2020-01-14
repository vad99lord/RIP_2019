class FigureColor:
    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color_val):
        self._color = color_val

    @color.getter
    def color(self):
        return self._color
