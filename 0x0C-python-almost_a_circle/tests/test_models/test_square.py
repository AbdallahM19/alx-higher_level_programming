#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        square = Square(5)
        self.assertEqual(square.id, 11)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square = Square(7, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_str_method(self):
        square = Square(5, 2, 3, 7)
        self.assertEqual(str(square), "[Square] (7) 2/3 - 5")

        square.size = 8
        square.x = 12
        square.y = 8
        self.assertEqual(str(square), "[Square] (7) 12/8 - 8")

    def test_update_method_args(self):
        square = Square(5)
        square.update(1, 15, 20, 25)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)

        with self.assertRaises(ValueError):
            square.update(1, -5, 10, 15)

    def test_update_method_kwargs(self):
        square = Square(5)
        square.update(size=15, x=20, y=25, id=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)

        with self.assertRaises(ValueError):
            square.update(size=-5, x=10, y=15)

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 7)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 7, 'size': 5, 'x': 2, 'y': 3})

        square.size = 8
        square.x = 12
        square.y = 8
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 7, 'size': 8, 'x': 12, 'y': 8})

    def test_area_method(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

        square.size = 8
        self.assertEqual(square.area(), 64)

        square.size = 10
        self.assertEqual(square.area(), 100)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            square = Square("invalid")

        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            square = Square(5, -2, 3)

        with self.assertRaises(ValueError):
            square = Square(5, 2, -3)

    def test_invalid_update_arguments(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(1, -5, 10, 15)

    def test_invalid_update_kwargs(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(size=-5, x=10, y=15)

"""---------------------------------------------"""



class TestSquare(unittest.TestCase):
    def test_id(self):
        s1 = Square(6, 4, 8, 34)
        s4 = Square(4, 9, 5, 40)

        self.assertEqual(s1.id, 34)
        self.assertEqual(s4.id, 40)
        self.assertEqual(s1.y, 4)

        s7 = Square(8, 6)
        s8 = Square(6, 4)
        self.assertEqual(s7.id, s8.id - 1)
        self.assertEqual(s7.size, 0)
        self.assertEqual(s8.x, 6)

        s1.size = 23
        self.assertEqual(s1.size, 23)

    def inheritance(self):
        self.assertIsInstance(Square(9), Base)

    def test_more_args(self):

        sec = Square(6)
        self.assertEqual(sec.y, 0)
        self.assertEqual(sec.x, 6)

        sec = Square(8, 7, 5)
        sec1 = Square(5, 4)
        self.assertEqual(sec.id, sec1.id - 1)


"""-----------------------------------------"""


class Square:
    id_counter = 0

    def __init__(self, x=0, y=0, size=0, id=None):
        self.x = x
        self.y = y
        self.size = size

        if id is not None:
            self.id = id
        else:
            self.id = Square.id_counter
            Square.id_counter += 1

    def __repr__(self):
        return f"Square({self.x}, {self.y}, {self.size}, {self.id})"

    def test_id(self):
        s1 = Square(6, 7, 8, 34)
        s4 = Square(4, 8, 5, 40)

        self.assertEqual(s1.id, 34)
        self.assertEqual(s4.id, 40)
        self.assertEqual(s1.y, 7)

        s7 = Square(8, 6)
        s8 = Square(6, 4)
        self.assertEqual(s7.id, s8.id - 1)
        self.assertEqual(s7.size, 8)
        self.assertEqual(s8.x, 4)

        s1.size = 23
        self.assertEqual(s1.size, 23)

    def inheritance(self):
        pass

    def test_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_more_args(self):
        s1 = Square(8, 7, 5)
        s2 = Square(5, 4)

        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.x, 4)

        s3 = Square(8, 6)
        self.assertEqual(s3.y, 6)
        self.assertEqual(s3.x, 8)

        s1.size = 23
        self.assertEqual(s1.size, 23)

if __name__ == "__main__":
    unittest.main()
