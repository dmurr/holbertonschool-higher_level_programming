#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square """
        self._size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of object """
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    @property
    def size(self):
        """ get size """
        return self._size

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update attributes """
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
        """ dictionary representation of attributes """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return (d)
