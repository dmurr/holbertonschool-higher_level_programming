#!/usr/bin/python3
"""
Module contains unittests for file base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        x1 = Base()
        self.assertEqual(x1.id, 1)
        self.assertEqual(x1.id, Base._Base__nb_objects)
        x2 = Base()
        self.assertEqual(x2.id, 2)
        self.assertEqual(x2.id, Base._Base__nb_objects)
        x3 = Base(44)
        self.assertEqual(x3.id, 44)
        x4 = Base()
        self.assertEqual(x4.id, 3)
        self.assertEqual(x4.id, Base._Base__nb_objects)
