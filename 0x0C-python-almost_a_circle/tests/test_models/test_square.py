#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io

class TestSquare(unittest.TestCase):
    '''Tests the Square class.'''

    def setUp(self):
        '''Set up test environment.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Test Square class type.'''
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Test if Square inherits from Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Test constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Test constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Test instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
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
        '''Test positional instantiation.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Test positional instantiation.'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Test if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Test property getters/setters.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    # ----------------- Tests for #3 ------------------------

    def invalid_types(self):
        '''Return tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Test property validation.'''
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
        '''Test property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Test property validation.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Test property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Test property setting/getting.'''
        r = Square(1, 2)
        attributes = ["x", "y", "size"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Test property setting/getting.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------------- Tests for #4 ------------------------
    def test_I_area_no_args(self):
        '''Test area() method signature.'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Test area() method computation.'''
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

    # ----------------- Tests for #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Test display() method signature.'''
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Test display() method output.'''
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

    # ----------------- Tests for #6 ------------------------
    def test_K_str_no_args(self):
        '''Test __str__() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Test __str__() method return.'''
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)

    # ----------------- Tests for #8 & #9 ------------------------
    def test_L_update_no_args(self):
        '''Test update() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_L_update_args(self):
        '''Test update() positional args.'''
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
        '''Test update() positional arg fubars.'''
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
        '''Test update() keyword args.'''
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

    def test_L_update_kwargs_bad(self):
        '''Test update() keyword arg fubars.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        with self.assertRaises(ValueError) as e:
            r.update(size=-17)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(x=-20)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(y=-25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(size=0)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_L_update_args_kwargs(self):
        '''Test update() combined args/kwargs.'''
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(10, size=17)
        d["id"] = 10
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(20, 25, x=30)
        d["id"] = 20
        d["_Rectangle__height"] = 25
        d["_Rectangle__width"] = 25
        d["_Rectangle__x"] = 30
        self.assertEqual(r.__dict__, d)

        r.update(30, 35, 40, y=45)
        d["id"] = 30
        d["_Rectangle__height"] = 35
        d["_Rectangle__width"] = 35
        d["_Rectangle__x"] = 40
        d["_Rectangle__y"] = 45
        self.assertEqual(r.__dict__, d)

    # ----------------- Tests for #10 ------------------------
    def test_M_to_dictionary_no_args(self):
        '''Test to_dictionary() method signature.'''
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        self.assertDictEqual(Square.to_dictionary(r), d)

    def test_M_to_dictionary_simple(self):
        '''Test to_dictionary() method returns dict.'''
        r = Square(5, 2)
        d = r.__dict__.copy()
        self.assertDictEqual(Square.to_dictionary(r), d)

        r = Square(5, 2, 3)
        d = r.__dict__.copy()
        self.assertDictEqual(Square.to_dictionary(r), d)

        r = Square(5, 2, 3, 4)
        d = r.__dict__.copy()
        self.assertDictEqual(Square.to_dictionary(r), d)

    def test_M_save_to_file(self):
        '''Test class method save_to_file().'''
        Base._Base__nb_objects = 0
        r1 = Square(5)
        r2 = Square(7, 9)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"y": 0, "x": 0, "id": 1, "size": 5}, {"y": 0, "x": 9, "id": 2, "size": 7}]')

        r3 = Square(1, 2)
        Square.save_to_file([r3])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"y": 0, "x": 0, "id": 1, "size": 5}, {"y": 0, "x": 9, "id": 2, "size": 7}, {"y": 0, "x": 2, "id": 3, "size": 1}]')

        r4 = Square(3, 4, 5, 6)
        Square.save_to_file([r4])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"y": 0, "x": 0, "id": 1, "size": 5}, {"y": 0, "x": 9, "id": 2, "size": 7}, {"y": 0, "x": 2, "id": 3, "size": 1}, {"y": 5, "x": 4, "id": 6, "size": 3}]')

        r5 = Square(1, 1, 1, 1)
        Square.save_to_file([r5])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"y": 0, "x": 0, "id": 1, "size": 5}, {"y": 0, "x": 9, "id": 2, "size": 7}, {"y": 0, "x": 2, "id": 3, "size": 1}, {"y": 5, "x": 4, "id": 6, "size": 3}, {"y": 1, "x": 1, "id": 1, "size": 1}]')

        r6 = Square(7)
        Square.save_to_file([r6])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"y": 0, "x": 0, "id": 1, "size": 5}, {"y": 0, "x": 9, "id": 2, "size": 7}, {"y": 0, "x": 2, "id": 3, "size": 1}, {"y": 5, "x": 4, "id": 6, "size": 3}, {"y": 1, "x": 1, "id": 1, "size": 1}, {"y": 0, "x": 0, "id": 7, "size": 7}]')

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')

    # ----------------- Tests for #12 ------------------------
    def test_N_load_from_file(self):
        '''Test class method load_from_file().'''
        r = Square(5, 2)
        r1 = Square(7, 9)
        Square.save_to_file([r, r1])
        lst = Square.load_from_file()
        self.assertEqual(lst[0].size, 5)
        self.assertEqual(lst[0].x, 2)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].size, 7)
        self.assertEqual(lst[1].x, 9)
        self.assertEqual(lst[1].y, 0)

        r3 = Square(1, 2)
        Square.save_to_file([r3])
        lst = Square.load_from_file()
        self.assertEqual(lst[2].size, 1)
        self.assertEqual(lst[2].x, 2)
        self.assertEqual(lst[2].y, 0)

        r4 = Square(3, 4, 5, 6)
        Square.save_to_file([r4])
        lst = Square.load_from_file()
        self.assertEqual(lst[3].size, 3)
        self.assertEqual(lst[3].x, 4)
        self.assertEqual(lst[3].y, 5)
        self.assertEqual(lst[3].id, 6)

        r5 = Square(1, 1, 1, 1)
        Square.save_to_file([r5])
        lst = Square.load_from_file()
        self.assertEqual(lst[4].size, 1)
        self.assertEqual(lst[4].x, 1)
        self.assertEqual(lst[4].y, 1)
        self.assertEqual(lst[4].id, 1)

        r6 = Square(7)
        Square.save_to_file([r6])
        lst = Square.load_from_file()
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 0)
        self.assertEqual(lst[5].y, 0)
        self.assertEqual(lst[5].id, 7)

        lst = Square.load_from_file()
        self.assertEqual(lst[0].size, 5)
        self.assertEqual(lst[0].x, 2)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].size, 7)
        self.assertEqual(lst[1].x, 9)
        self.assertEqual(lst[1].y, 0)
        self.assertEqual(lst[2].size, 1)
        self.assertEqual(lst[2].x, 2)
        self.assertEqual(lst[2].y, 0)
        self.assertEqual(lst[3].size, 3)
        self.assertEqual(lst[3].x, 4)
        self.assertEqual(lst[3].y, 5)
        self.assertEqual(lst[3].id, 6)
        self.assertEqual(lst[4].size, 1)
        self.assertEqual(lst[4].x, 1)
        self.assertEqual(lst[4].y, 1)
        self.assertEqual(lst[4].id, 1)
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 0)
        self.assertEqual(lst[5].y, 0)
        self.assertEqual(lst[5].id, 7)

        r7 = Square(2, 2)
        Square.save_to_file([r7])
        lst = Square.load_from_file()
        self.assertEqual(lst[6].size, 2)
        self.assertEqual(lst[6].x, 2)
        self.assertEqual(lst[6].y, 0)
        self.assertEqual(lst[6].id, 1)
        self.assertEqual(lst[0].id, 8)
        self.assertEqual(lst[1].id, 9)
        self.assertEqual(lst[2].id, 10)
        self.assertEqual(lst[3].id, 11)
        self.assertEqual(lst[4].id, 12)
        self.assertEqual(lst[5].id, 13)
        self.assertEqual(lst[6].id, 14)

    # ----------------- Tests for #13 ------------------------
    def test_O_save_to_file_csv(self):
        '''Test class method save_to_file_csv().'''
        Base._Base__nb_objects = 0
        r1 = Square(5)
        r2 = Square(7, 9)
        Square.save_to_file_csv([r1, r2])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n")

        r3 = Square(1, 2)
        Square.save_to_file_csv([r3])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n3,1,2,0\n")

        r4 = Square(3, 4, 5, 6)
        Square.save_to_file_csv([r4])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n3,1,2,0\n4,3,4,5\n")

        r5 = Square(1, 1, 1, 1)
        Square.save_to_file_csv([r5])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n3,1,2,0\n4,3,4,5\n5,1,1,1\n")

        r6 = Square(7)
        Square.save_to_file_csv([r6])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n3,1,2,0\n4,3,4,5\n5,1,1,1\n6,7,0,0\n")

        r7 = Square(2, 2)
        Square.save_to_file_csv([r7])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "id,size,x,y\n1,5,0,0\n2,7,9,0\n3,1,2,0\n4,3,4,5\n5,1,1,1\n6,7,0,0\n7,2,2,0\n")

    # ----------------- Tests for #14 ------------------------
    def test_P_load_from_file_csv(self):
        '''Test class method load_from_file_csv().'''
        r = Square(5, 2)
        r1 = Square(7, 9)
        Square.save_to_file_csv([r, r1])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[0].size, 5)
        self.assertEqual(lst[0].x, 2)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].size, 7)
        self.assertEqual(lst[1].x, 9)
        self.assertEqual(lst[1].y, 0)

        r3 = Square(1, 2)
        Square.save_to_file_csv([r3])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[2].size, 1)
        self.assertEqual(lst[2].x, 2)
        self.assertEqual(lst[2].y, 0)

        r4 = Square(3, 4, 5, 6)
        Square.save_to_file_csv([r4])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[3].size, 3)
        self.assertEqual(lst[3].x, 4)
        self.assertEqual(lst[3].y, 5)
        self.assertEqual(lst[3].id, 6)

        r5 = Square(1, 1, 1, 1)
        Square.save_to_file_csv([r5])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[4].size, 1)
        self.assertEqual(lst[4].x, 1)
        self.assertEqual(lst[4].y, 1)
        self.assertEqual(lst[4].id, 1)

        r6 = Square(7)
        Square.save_to_file_csv([r6])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 0)
        self.assertEqual(lst[5].y, 0)
        self.assertEqual(lst[5].id, 7)

        lst = Square.load_from_file_csv()
        self.assertEqual(lst[0].size, 5)
        self.assertEqual(lst[0].x, 2)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].size, 7)
        self.assertEqual(lst[1].x, 9)
        self.assertEqual(lst[1].y, 0)
        self.assertEqual(lst[2].size, 1)
        self.assertEqual(lst[2].x, 2)
        self.assertEqual(lst[2].y, 0)
        self.assertEqual(lst[3].size, 3)
        self.assertEqual(lst[3].x, 4)
        self.assertEqual(lst[3].y, 5)
        self.assertEqual(lst[3].id, 6)
        self.assertEqual(lst[4].size, 1)
        self.assertEqual(lst[4].x, 1)
        self.assertEqual(lst[4].y, 1)
        self.assertEqual(lst[4].id, 1)
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 0)
        self.assertEqual(lst[5].y, 0)
        self.assertEqual(lst[5].id, 7)

        r7 = Square(2, 2)
        Square.save_to_file_csv([r7])
        lst = Square.load_from_file_csv()
        self.assertEqual(lst[6].size, 2)
        self.assertEqual(lst[6].x, 2)
        self.assertEqual(lst[6].y, 0)
        self.assertEqual(lst[6].id, 1)
        self.assertEqual(lst[0].id, 8)
        self.assertEqual(lst[1].id, 9)
        self.assertEqual(lst[2].id, 10)
        self.assertEqual(lst[3].id, 11)
        self.assertEqual(lst[4].id, 12)
        self.assertEqual(lst[5].id, 13)
        self.assertEqual(lst[6].id, 14)

    def test_P_load_from_file_csv_no_file(self):
        '''Test load_from_file_csv() with no file.'''
        os.remove("Square.csv")
        self.assertEqual(Square.load_from_file_csv(), [])

    def test_P_load_from_file_csv_no_id(self):
        '''Test load_from_file_csv() with no id field.'''
        os.remove("Square.csv")
        with open("Square.csv", "w") as f:
            f.write("size,x,y\n")
        with self.assertRaises(KeyError) as e:
            Square.load_from_file_csv()
        s = "'id'"
        self.assertIn(s, str(e.exception))

    def test_P_load_from_file_csv_no_size(self):
        '''Test load_from_file_csv() with no size field.'''
        os.remove("Square.csv")
        with open("Square.csv", "w") as f:
            f.write("id,x,y\n")
        with self.assertRaises(KeyError) as e:
            Square.load_from_file_csv()
        s = "'size'"
        self.assertIn(s, str(e.exception))

    def test_P_load_from_file_csv_no_x(self):
        '''Test load_from_file_csv() with no x field.'''
        os.remove("Square.csv")
        with open("Square.csv", "w") as f:
            f.write("id,size,y\n")
        with self.assertRaises(KeyError) as e:
            Square.load_from_file_csv()
        s = "'x'"
        self.assertIn(s, str(e.exception))

    def test_P_load_from_file_csv_no_y(self):
        '''Test load_from_file_csv() with no y field.'''
        os.remove("Square.csv")
        with open("Square.csv", "w") as f:
            f.write("id,size,x\n")
        with self.assertRaises(KeyError) as e:
            Square.load_from_file_csv()
        s = "'y'"
        self.assertIn(s, str(e.exception))

    def test_P_load_from_file_csv_dup_id(self):
        '''Test load_from_file_csv() with duplicate id values.'''
        os.remove("Square.csv")
        with open("Square.csv", "w") as f:
            f.write("id,size,x,y\n")
            f.write("1,5,2,0\n")
            f.write("1,5,2,0\n")
        with self.assertRaises(ValueError) as e:
            Square.load_from_file_csv()
        s = "Multiple objects with same id: 1"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #16 ------------------------
    def test_R_save_to_file_csv_None(self):
        '''Test save_to_file_csv() with None list.'''
        os.remove("Square.csv")
        with self.assertRaises(TypeError) as e:
            Square.save_to_file_csv(None)
        s = "save_to_file_csv() argument must be a list of Base objects"
        self.assertEqual(str(e.exception), s)

    def test_R_save_to_file_csv_list_empty(self):
        '''Test save_to_file_csv() with empty list.'''
        os.remove("Square.csv")
        Square.save_to_file_csv([])
        self.assertTrue(os.path.isfile("Square.csv"))
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "")

    def test_R_save_to_file_None(self):
        '''Test save_to_file() with None list.'''
        os.remove("Square.json")
        with self.assertRaises(TypeError) as e:
            Square.save_to_file(None)
        s = "save_to_file() argument must be a list of Base objects"
        self.assertEqual(str(e.exception), s)

    def test_R_save_to_file_list_empty(self):
        '''Test save_to_file() with empty list.'''
        os.remove("Square.json")
        Square.save_to_file([])
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    # ----------------- Tests for #17 ------------------------
    def test_S_save_to_file_rectangles(self):
        '''Test save_to_file() for Rectangle objects.'''
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4, 5, 6)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"height": 2, "width": 1, "id": 1, "x": 0, "y": 0}, {"height": 4, "width": 3, "id": 2, "x": 5, "y": 6}]')

    def test_S_load_from_file_rectangles(self):
        '''Test load_from_file() for Rectangle objects.'''
        r = Rectangle(5, 2)
        r1 = Rectangle(7, 9)
        Rectangle.save_to_file([r, r1])
        lst = Rectangle.load_from_file()
        self.assertEqual(lst[0].width, 5)
        self.assertEqual(lst[0].height, 2)
        self.assertEqual(lst[0].x, 0)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].width, 7)
        self.assertEqual(lst[1].height, 9)
        self.assertEqual(lst[1].x, 0)
        self.assertEqual(lst[1].y, 0)

    # ----------------- Tests for #19 ------------------------
    def test_U_save_to_file_update_create(self):
        '''Test save_to_file() after update() creates object.'''
        Base._Base__nb_objects = 0
        r = Square(5)
        r1 = Square(7, 9)
        r2 = Square(1, 2)
        r3 = Square(3, 4, 5, 6)
        r4 = Square(1, 1, 1, 1)
        r5 = Square(7)
        r6 = Square(2, 2)
        r7 = Square(8)
        Square.save_to_file([r, r1, r2, r3, r4, r5, r6, r7])
        lst = Square.load_from_file()
        self.assertEqual(lst[0].size, 5)
        self.assertEqual(lst[0].x, 0)
        self.assertEqual(lst[0].y, 0)
        self.assertEqual(lst[1].size, 7)
        self.assertEqual(lst[1].x, 9)
        self.assertEqual(lst[1].y, 0)
        self.assertEqual(lst[2].size, 1)
        self.assertEqual(lst[2].x, 2)
        self.assertEqual(lst[2].y, 0)
        self.assertEqual(lst[3].size, 3)
        self.assertEqual(lst[3].x, 4)
        self.assertEqual(lst[3].y, 5)
        self.assertEqual(lst[4].size, 1)
        self.assertEqual(lst[4].x, 1)
        self.assertEqual(lst[4].y, 1)
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 0)
        self.assertEqual(lst[5].y, 0)
        self.assertEqual(lst[6].size, 2)
        self.assertEqual(lst[6].x, 2)
        self.assertEqual(lst[6].y, 0)
        self.assertEqual(lst[7].size, 8)
        self.assertEqual(lst[7].x, 0)
        self.assertEqual(lst[7].y, 0)
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[1].id, 2)
        self.assertEqual(lst[2].id, 3)
        self.assertEqual(lst[3].id, 6)
        self.assertEqual(lst[4].id, 1)
        self.assertEqual(lst[5].id, 7)
        self.assertEqual(lst[6].id, 8)
        self.assertEqual(lst[7].id, 9)

    def test_U_save_to_file_update_modify(self):
        '''Test save_to_file() after update() modifies object.'''
        Base._Base__nb_objects = 0
        r = Square(5)
        r1 = Square(7, 9)
        r2 = Square(1, 2)
        r3 = Square(3, 4, 5, 6)
        r4 = Square(1, 1, 1, 1)
        r5 = Square(7)
        r6 = Square(2, 2)
        r7 = Square(8)
        r.update(1, 99, 98, 97, 96)
        r1.update(2, 999)
        r2.update(3, 9, 8, 7)
        r3.update(6, 6)
        r4.update(1, 2, 3, 4)
        r5.update(7, 7, 7, 7)
        r6.update(2, 2, 2, 2)
        r7.update(8, 8)
        Square.save_to_file([r, r1, r2, r3, r4, r5, r6, r7])
        lst = Square.load_from_file()
        self.assertEqual(lst[0].size, 99)
        self.assertEqual(lst[0].x, 98)
        self.assertEqual(lst[0].y, 97)
        self.assertEqual(lst[1].size, 999)
        self.assertEqual(lst[1].x, 0)
        self.assertEqual(lst[1].y, 0)
        self.assertEqual(lst[2].size, 9)
        self.assertEqual(lst[2].x, 8)
        self.assertEqual(lst[2].y, 7)
        self.assertEqual(lst[3].size, 6)
        self.assertEqual(lst[3].x, 0)
        self.assertEqual(lst[3].y, 0)
        self.assertEqual(lst[4].size, 2)
        self.assertEqual(lst[4].x, 3)
        self.assertEqual(lst[4].y, 4)
        self.assertEqual(lst[5].size, 7)
        self.assertEqual(lst[5].x, 7)
        self.assertEqual(lst[5].y, 7)
        self.assertEqual(lst[6].size, 2)
        self.assertEqual(lst[6].x, 2)
        self.assertEqual(lst[6].y, 2)
        self.assertEqual(lst[7].size, 8)
        self.assertEqual(lst[7].x, 0)
        self.assertEqual(lst[7].y, 0)
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[1].id, 2)
        self.assertEqual(lst[2].id, 3)
        self.assertEqual(lst[3].id, 6)
        self.assertEqual(lst[4].id, 1)
        self.assertEqual(lst[5].id, 7)
        self.assertEqual(lst[6].id, 2)
        self.assertEqual(lst[7].id, 8)

    # ----------------- Tests for #21 ------------------------
    def test_X_create_all_parameters(self):
        '''Test create() with all parameters.'''
        Base._Base__nb_objects = 0
        d = {"id": 99, "size": 88, "x": 77, "y": 66}
        r = Square.create(**d)
        self.assertTrue(type(r) is Square)
        self.assertEqual(r.size, 88)
        self.assertEqual(r.x, 77)
        self.assertEqual(r.y, 66)
        self.assertEqual(r.id, 99)

    def test_X_create_no_parameters(self):
        '''Test create() with no parameters.'''
        Base._Base__nb_objects = 0
        d = {}
        r = Square.create(**d)
        self.assertTrue(type(r) is Square)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_X_create_some_parameters(self):
        '''Test create() with some parameters.'''
        Base._Base__nb_objects = 0
        d = {"id": 99, "size": 88}
        r = Square.create(**d)
        self.assertTrue(type(r) is Square)
        self.assertEqual(r.size, 88)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 99)

    def test_X_create_extra_parameters(self):
        '''Test create() with extra parameters.'''
        Base._Base__nb_objects = 0
        d = {"id": 99, "size": 88, "x": 77, "y": 66, "w": 55}
        with self.assertRaises(TypeError) as e:
            r = Square.create(**d)
        s = "create() takes from 1 to 4 positional arguments but 5 were given"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #23 ------------------------
    def test_Y_update_args_empty(self):
        '''Test update() with no arguments.'''
        r = Square(5)
        r.update()
        self.assertEqual(str(r), "[Square] (1) 0/0 - 5")

    def test_Y_update_args_one(self):
        '''Test update() with one argument.'''
        r = Square(5)
        r.update(99)
        self.assertEqual(str(r), "[Square] (99) 0/0 - 5")

    def test_Y_update_args_two(self):
        '''Test update() with two arguments.'''
        r = Square(5)
        r.update(99, 88)
        self.assertEqual(str(r), "[Square] (99) 0/0 - 88")

    def test_Y_update_args_three(self):
        '''Test update() with three arguments.'''
        r = Square(5)
        r.update(99, 88, 77)
        self.assertEqual(str(r), "[Square] (99) 77/0 - 88")

    def test_Y_update_args_four(self):
        '''Test update() with four arguments.'''
        r = Square(5)
        r.update(99, 88, 77, 66)
        self.assertEqual(str(r), "[Square] (99) 77/66 - 88")

    def test_Y_update_args_five(self):
        '''Test update() with five arguments.'''
        r = Square(5)
        r.update(99, 88, 77, 66, 55)
        self.assertEqual(str(r), "[Square] (99) 77/66 - 88")

    # ----------------- Tests for #24 ------------------------
    def test_Z_update_kwargs_no_args(self):
        '''Test update() with no kwargs.'''
        r = Square(5)
        r.update()
        self.assertEqual(str(r), "[Square] (1) 0/0 - 5")

    def test_Z_update_kwargs_one_arg(self):
        '''Test update() with one kwarg.'''
        r = Square(5)
        r.update(size=99)
        self.assertEqual(str(r), "[Square] (1) 0/0 - 99")

    def test_Z_update_kwargs_two_args(self):
        '''Test update() with two kwargs.'''
        r = Square(5)
        r.update(size=99, x=88)
        self.assertEqual(str(r), "[Square] (1) 88/0 - 99")

    def test_Z_update_kwargs_three_args(self):
        '''Test update() with three kwargs.'''
        r = Square(5)
        r.update(size=99, x=88, y=77)
        self.assertEqual(str(r), "[Square] (1) 88/77 - 99")

    def test_Z_update_kwargs_four_args(self):
        '''Test update() with four kwargs.'''
        r = Square(5)
        r.update(size=99, x=88, y=77, id=66)
        self.assertEqual(str(r), "[Square] (66) 88/77 - 99")

    def test_Z_update_kwargs_extra_args(self):
        '''Test update() with extra kwargs.'''
        r = Square(5)
        r.update(size=99, x=88, y=77, id=66, w=55)
        self.assertEqual(str(r), "[Square] (66) 88/77 - 99")

    def test_Z_update_kwargs_bad_arg(self):
        '''Test update() with bad kwarg.'''
        r = Square(5)
        r.update(size=99, x=88, y=77, bad=66)
        self.assertEqual(str(r), "[Square] (1) 88/77 - 99")

    def test_Z_update_kwargs_id_0(self):
        '''Test update() with id set to 0.'''
        r = Square(5)
        r.update(id=0)
        self.assertEqual(str(r), "[Square] (0) 0/0 - 5")

    def test_Z_update_args_and_kwargs(self):
        '''Test update() with both args and kwargs.'''
        r = Square(5)
        r.update(99, 88, 77, size=66, x=55, y=44)
        self.assertEqual(str(r), "[Square] (99) 77/0 - 88")

    def test_Z_update_args_and_kwargs_wrong_order(self):
        '''Test update() with both args and kwargs in reverse order.'''
        r = Square(5)
        r.update(size=99, x=88, y=77, 88, 77, 66)
        self.assertEqual(str(r), "[Square] (66) 88/77 - 77")

    # ----------------- Tests for #25 ------------------------
    def test_Z_update_args_and_kwargs_wrong_arg(self):
        '''Test update() with both args and kwargs and a kwarg that clashes with an arg.'''
        r = Square(5)
        r.update(99, 88, size=77)
        self.assertEqual(str(r), "[Square] (99) 88/0 - 88")

    # ----------------- Tests for #26 ------------------------
    def test_T_update_args_int_width(self):
        '''Test update() with args, width is an int.'''
        r = Square(5)
        r.update(99, 88, 77, 55)
        self.assertEqual(str(r), "[Square] (99) 88/77 - 55")

    def test_T_update_args_float_width(self):
        '''Test update() with args, width is a float.'''
        r = Square(5)
        r.update(99, 88, 77, 55.5)
        self.assertEqual(str(r), "[Square] (99) 88/77 - 55.5")

    def test_T_update_args_bool_width(self):
        '''Test update() with args, width is a bool.'''
        r = Square(5)
        r.update(99, 88, 77, True)
        self.assertEqual(str(r), "[Square] (99) 88/77 - 1")

    def test_T_update_args_str_width(self):
        '''Test update() with args, width is a str.'''
        r = Square(5)
        r.update(99, 88, 77, "55")
        self.assertEqual(str(r), "[Square] (99) 88/77 - 55")

    # ----------------- Tests for #28 ------------------------
    def test_R_to_dictionary_square(self):
        '''Test to_dictionary() for Square.'''
        r = Square(5, 6, 7, 8)
        d = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_R_to_dictionary_square_default(self):
        '''Test to_dictionary() for Square with default values.'''
        r = Square(1)
        d = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(r.to_dictionary(), d)

    # ----------------- Tests for #29 ------------------------
    def test_S_from_json_string_no_file(self):
        '''Test from_json_string() with no file.'''
        os.remove("Square.json")
        self.assertEqual(Square.from_json_string(), [])

    def test_S_from_json_string_empty_file(self):
        '''Test from_json_string() with empty file.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write("")
        self.assertEqual(Square.from_json_string(), [])

    def test_S_from_json_string_one_dict(self):
        '''Test from_json_string() with one dictionary.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}]')
        lst = Square.from_json_string()
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[0].size, 2)
        self.assertEqual(lst[0].x, 3)
        self.assertEqual(lst[0].y, 4)

    def test_S_from_json_string_multiple_dicts(self):
        '''Test from_json_string() with multiple dictionaries.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')
        lst = Square.from_json_string()
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[0].size, 2)
        self.assertEqual(lst[0].x, 3)
        self.assertEqual(lst[0].y, 4)
        self.assertEqual(lst[1].id, 5)
        self.assertEqual(lst[1].size, 6)
        self.assertEqual(lst[1].x, 7)
        self.assertEqual(lst[1].y, 8)

    def test_S_to_json_string_no_file(self):
        '''Test to_json_string() with no file.'''
        os.remove("Square.json")
        self.assertEqual(Square.to_json_string([]), "[]")

    def test_S_to_json_string_empty_file(self):
        '''Test to_json_string() with empty list.'''
        os.remove("Square.json")
        self.assertEqual(Square.to_json_string([]), "[]")

    def test_S_to_json_string_one_dict(self):
        '''Test to_json_string() with one dictionary.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}]')
        lst = Square.to_json_string([Square(1, 2, 3, 4)])
        self.assertEqual(lst, '[{"id": 1, "size": 2, "x": 3, "y": 4}]')

    def test_S_to_json_string_multiple_dicts(self):
        '''Test to_json_string() with multiple dictionaries.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')
        lst = Square.to_json_string([Square(1, 2, 3, 4), Square(5, 6, 7, 8)])
        self.assertEqual(lst, '[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')

    def test_S_to_json_string_bad_param(self):
        '''Test to_json_string() with a bad argument.'''
        os.remove("Square.json")
        with self.assertRaises(TypeError) as e:
            Square.to_json_string(Square(5, 6, 7, 8))
        s = "to_json_string() argument must be a list of objects"
        self.assertEqual(str(e.exception), s)

    def test_S_to_json_string_extra_param(self):
        '''Test to_json_string() with an extra parameter.'''
        os.remove("Square.json")
        with self.assertRaises(TypeError) as e:
            Square.to_json_string([Square(5, 6, 7, 8)], 99)
        s = "to_json_string() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), s)

    # ----------------- Tests for #30 ------------------------
    def test_S_from_file_json_no_file(self):
        '''Test from_file() with no file.'''
        os.remove("Square.json")
        self.assertEqual(Square.from_file(), [])

    def test_S_from_file_json_empty_file(self):
        '''Test from_file() with empty file.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write("")
        self.assertEqual(Square.from_file(), [])

    def test_S_from_file_json_one_dict(self):
        '''Test from_file() with one dictionary.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}]')
        lst = Square.from_file()
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[0].size, 2)
        self.assertEqual(lst[0].x, 3)
        self.assertEqual(lst[0].y, 4)

    def test_S_from_file_json_multiple_dicts(self):
        '''Test from_file() with multiple dictionaries.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')
        lst = Square.from_file()
        self.assertEqual(lst[0].id, 1)
        self.assertEqual(lst[0].size, 2)
        self.assertEqual(lst[0].x, 3)
        self.assertEqual(lst[0].y, 4)
        self.assertEqual(lst[1].id, 5)
        self.assertEqual(lst[1].size, 6)
        self.assertEqual(lst[1].x, 7)
        self.assertEqual(lst[1].y, 8)

    def test_S_to_file_json_no_file(self):
        '''Test to_file() with no file.'''
        os.remove("Square.json")
        self.assertEqual(Square.to_file([]), "[]")

    def test_S_to_file_json_empty_file(self):
        '''Test to_file() with empty list.'''
        os.remove("Square.json")
        self.assertEqual(Square.to_file([]), "[]")

    def test_S_to_file_json_one_dict(self):
        '''Test to_file() with one dictionary.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}]')
        lst = Square.to_file([Square(1, 2, 3, 4)])
        self.assertEqual(lst, '[{"id": 1, "size": 2, "x": 3, "y": 4}]')

    def test_S_to_file_json_multiple_dicts(self):
        '''Test to_file() with multiple dictionaries.'''
        os.remove("Square.json")
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')
        lst = Square.to_file([Square(1, 2, 3, 4), Square(5, 6, 7, 8)])
        self.assertEqual(lst, '[{"id": 1, "size": 2, "x": 3, "y": 4}, {"id": 5, "size": 6, "x": 7, "y": 8}]')

    def test_S_to_file_json_bad_param(self):
        '''Test to_file() with a bad argument.'''
        os.remove("Square.json")
        with self.assertRaises(TypeError) as e:
            Square.to_file(Square(5, 6, 7, 8))
        s = "to_file() argument must be a list of objects"
        self.assertEqual(str(e.exception), s)

    def test_S_to_file_json_extra_param(self):
        '''Test to_file() with an extra parameter.'''
        os.remove("Square.json")
        with self.assertRaises(TypeError) as e:
            Square.to_file([Square(5, 6, 7, 8)], 99)
        s = "to_file() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), s)

if __name__ == '__main__':
    unittest.main()

