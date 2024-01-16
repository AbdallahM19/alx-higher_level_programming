#!/usr/bin/python3
'''Module for AnotherBase unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import inspect


class TestAnotherBase(unittest.TestCase):
    '''Tests the AnotherBase class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests AnotherBase() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_F_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Tests id passed as keyword arg.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)
        Rectangle.save_to_file(None)

    def test_J_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

    def test_L_custom_id_float(self):
        '''Tests custom float id.'''
        i = 98.5
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_M_custom_id_boolean(self):
        '''Tests custom boolean id.'''
        i = True
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_N_custom_id_list(self):
        '''Tests custom list id.'''
        i = [1, 2, 3]
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_O_to_json_string_empty_list(self):
        '''Tests to_json_string() with an empty list.'''
        self.assertEqual(Base.to_json_string([]), [])

    def test_P_from_json_string_empty_string(self):
        '''Tests from_json_string() with an empty string.'''
        self.assertEqual(Base.from_json_string(""), [])


'''-----------------------------------------'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Sending a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            Sending an id that is not an int
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
            Sending an id that is not an int
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
            Sending an id that is not an int
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
            Sending an id that is not an int
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        '''
            Testing the json string
        '''
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, [])

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, [])


class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

-------------------------------------------------


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):

        rectangle = Base()
        self.assertEqual(rectangle.id, 1)

        rectangle = Base(98)
        self.assertEqual(rectangle.id, 98)

        rectangle = Base()
        self.assertEqual(rectangle.id, 2)

        base = Base(98)
        base.id = 70
        self.assertEqual(base.id, 70)

        self.assertEqual("test", Base("test").id)
        self.assertEqual(33.3, Base(33.3).id)

        with self.assertRaises(TypeError):
            base = Base(4, 8)

    def test_ides(self):
        b1 = Base(67)
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 67)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_to_json(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        list = [{"id": 4}, {"id": 6}]
        json_string = '[{"id": 4}, {"id": 6}]'
        self.assertEqual(Base.to_json_string(list), json_string)

    def test_error(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

if __name__ == "__main__":
    unittest.main()
