#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

class TestRectangle(unittest.TestCase):
    '''Tests the Rectangle class.'''

    def setUp(self):
        '''Set up the test environment.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Test the type of the Rectangle class.'''
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Test if Rectangle inherits from Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Test constructor signature with no arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Test constructor signature with too many arguments.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were given"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''Test constructor signature with only one argument.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Test instantiation of Rectangle.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        # ... (other test cases)

    def test_D_instantiation_positional(self):
        '''Test positional instantiation.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Test keyword instantiation.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Test if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Test property getters/setters.'''
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ... (other test cases)

if __name__ == "__main__":
    unittest.main()

