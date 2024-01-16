#!/usr/bin/python3
from contextlib import redirect_stdout
import inspect
import io
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json
from io import StringIO
import sys


"""class"""


class TestRectangle(unittest.TestCase):
    """class"""
    def test_constructor(self):
        rect = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 30)
        self.assertEqual(rect.y, 40)
        self.assertEqual(rect.id, 1)

    def test_width_setter(self):
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_setter(self):
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -5

    def test_x_setter(self):
        rect = Rectangle(5, 10)
        rect.x = 15
        self.assertEqual(rect.x, 15)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y_setter(self):
        rect = Rectangle(5, 10)
        rect.y = 20
        self.assertEqual(rect.y, 20)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5

    def test_area_method(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

        rect.width = 3
        rect.height = 7
        self.assertEqual(rect.area(), 21)

    def test_str_method(self):
        rect = Rectangle(5, 10, 2, 3, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 2/3 - 5/10")

        rect.width = 8
        rect.height = 15
        rect.id = 12
        self.assertEqual(str(rect), "[Rectangle] (12) 2/3 - 8/15")

    def test_update_method_args(self):
        rect = Rectangle(5, 10)
        rect.update(1, 15, 20, 25, 30)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 25)
        self.assertEqual(rect.y, 30)

        with self.assertRaises(ValueError):
            rect.update(1, -5, 10, 15, 20)

    def test_update_method_kwargs(self):
        rect = Rectangle(5, 10)
        rect.update(width=15, height=20, x=25, y=30, id=1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 25)
        self.assertEqual(rect.y, 30)

        with self.assertRaises(ValueError):
            rect.update(width=-5, height=10, x=15, y=20)

    def test_to_dictionary_method(self):
        rect = Rectangle(5, 10, 2, 3, 7)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {
          'id': 7, 'width': 5, 'height': 10, 'x': 2, 'y': 3
        })

        rect.width = 8
        rect.height = 15
        rect.x = 12
        rect.y = 8
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {
          'id': 7, 'width': 8, 'height': 15, 'x': 12, 'y': 8
        })
