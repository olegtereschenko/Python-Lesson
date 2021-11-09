class Road:
    def __int__(self, length, width):
        self._length = length
        self._width = width

    def the_end(self, weight=25, depth=5):
        return f'{self._length}м.*{self._width}м.*{weight}*{depth}см.=' \
               f'{(self._length * self._width * weight * depth) / 1000}т.'


road_first = Road(5000,20)
print(road_first.the_end())
