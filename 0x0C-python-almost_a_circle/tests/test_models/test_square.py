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
        self.assertEqual(square_dict, {"id": 7, "size": 5, "x": 2, "y": 3})

        square.size = 8
        square.x = 12
        square.y = 8
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {"id": 7, "size": 8, "x": 12, "y": 8})

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
    """Tests the Base class."""

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_A_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        """Tests if Square inherits Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        """Tests instantiation."""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {
            "_Rectangle__height": 10,
            "_Rectangle__width": 10,
            "_Rectangle__x": 0,
            "_Rectangle__y": 0,
            "id": 1,
        }
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        """Tests positional instantiation."""
        r = Square(5, 10, 15)
        d = {
            "_Rectangle__height": 5,
            "_Rectangle__width": 5,
            "_Rectangle__x": 10,
            "_Rectangle__y": 15,
            "id": 1,
        }
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {
            "_Rectangle__height": 5,
            "_Rectangle__width": 5,
            "_Rectangle__x": 10,
            "_Rectangle__y": 15,
            "id": 20,
        }
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        """Tests positional instantiation."""
        r = Square(100, id=421, y=99, x=101)
        d = {
            "_Rectangle__height": 100,
            "_Rectangle__width": 100,
            "_Rectangle__x": 101,
            "_Rectangle__y": 99,
            "id": 421,
        }
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        """Tests if id is inherited from Base."""
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        """Tests property getters/setters."""
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {
            "_Rectangle__height": 98,
            "_Rectangle__width": 98,
            "_Rectangle__x": 102,
            "_Rectangle__y": 103,
            "id": 1,
        }
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        """Returns tuple of types for validation."""
        t = (
            3.14,
            -1.1,
            float("inf"),
            float("-inf"),
            True,
            "str",
            (2,),
            [4],
            {5},
            {6: 7},
            None,
        )
        return t

    def test_G_validate_type(self):
        """Tests property validation."""
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_I_area_no_args(self):
        """Tests area() method signature."""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        """Tests area() method compuation."""
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_J_display_no_args(self):
        """Tests display() method signature."""
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        """Tests display() method output."""
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










 #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
  ##
  ##
"""
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



 ###
 ###
 ###
"""
        self.assertEqual(f.getvalue(), s)

    def test_K_str_no_args(self):
        """Tests __str__() method signature."""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        """Tests __str__() method return."""
        r = Square(5)
        s = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = "[Square] (2) 1/0 - 1"
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = "[Square] (3) 4/5 - 3"
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = "[Square] (40) 20/30 - 10"
        self.assertEqual(str(r), s)

    def test_L_update_no_args(self):
        """Tests update() method signature."""
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_L_update_args(self):
        """Tests update() postional args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_args_bad(self):
        """Tests update() positional arg fubars."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_L_update_kwargs(self):
        """Tests update() keyword args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(size=17)
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_kwargs_2(self):
        """Tests update() keyword args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, size=5, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, x=20, size=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_M_to_dictionary(self):
        """Tests to_dictionary() signature:"""
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Square(1)
        d = {"x": 0, "y": 0, "size": 1, "id": 1}
        self.assertEqual(r.to_dictionary(), d)

        r = Square(9, 2, 3, 4)
        d = {"x": 2, "y": 3, "size": 9, "id": 4}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.size = 30
        d = {"x": 10, "y": 20, "size": 30, "id": 4}
        self.assertEqual(r.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()

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
