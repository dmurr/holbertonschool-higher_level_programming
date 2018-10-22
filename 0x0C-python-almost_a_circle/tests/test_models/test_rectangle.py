#!/usr/bin/python3
"""
unit test
"""
import unittest
from  models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ unit test for Rectangle class """

    def setUp(self):
        # self.shape1 = Rectangle(10, 2)
        pass

    def test_width(self):
        with self.assertRaises(TypeError):
            Rectangle.__init__(10, "str")
