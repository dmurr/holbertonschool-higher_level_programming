#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self._size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for i, k in enumerate(args):
                if i == 0:
                    self.id = k
                elif i == 1:
                    self._size = k
                elif i == 2:
                    self.x = k
                elif i == 3:
                    self.y = k
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self._size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return (d)
