#!/usr/bin/python3
"""
Contains Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle instance"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area """
        return self.width * self.height

    def display(self):
        """ displays rectangle """
        for c in range(self.y):
            print("")
        for a in range(self.height):
            d = self.x
            while d:
                print(" ", end="")
                d -= 1
            for i, b in enumerate(range(self.width)):
                if i < self.width - 1:
                    print("#", end="")
                else:
                    print("#")

    def __str__(self):
        """ string representation of object """
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width, self.height))

    def update(self, *args, **kwargs):
        """ update object attribute values """
        if args:
            for i, k in enumerate(args):
                if i == 0:
                    self.id = k
                elif i == 1:
                    self.__width = k
                elif i == 2:
                    self.__height = k
                elif i == 3:
                    self.__x = k
                elif i == 4:
                    self.__y = k
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.__width = v
                elif k == 'height':
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v

    def to_dictionary(self):
        """ convert to dictionary """
        d = {}
        d["id"] = self.id
        d["width"] = self.__width
        d["height"] = self.__height
        d["x"] = self.__x
        d["y"] = self.__y
        return (d)
