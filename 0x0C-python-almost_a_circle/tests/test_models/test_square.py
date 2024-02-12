#!/usr/bin/python3
# test_quarepy
"""
Test cases for class Rectangle
"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instatiation(unittest.TestCase):
    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_square(self):
        s1 = Square(10)
        s2 = Square(2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_all_args(self):
        s1 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 12)

    def test_id(self):
        s1 = Square(2)
        s2 = Square(10, 0, 0, 12)
        s3 = Square(10)
        self.assertEqual(s3.id, s1.id + 1)

    def test_2_args(self):
        s1 = Square(8, 9)
        s2 = Square(23, 1)
        self.assertEqual(s1.id, s2.id -1)

    def test_3_args(self):
        s1 = Square(7, 9, 0)
        s2 = Square(10, 1, 17)
        self.assertEqual(s1.id, s2.id -1)

    def test_4_args(self):
        self.assertEqual(10, Square(5, 0, 0, 10).id)

    def test_more_than_4_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(6, 0, 0, 1).__size)

    def test_size_getter(self):
        self.assertEqual(9, Square(9, 3, 4, 5).size)

    def test_size_setter(self):
        s = Square(7, 7, 5, 1)
        s.size = 13
        self.assertEqual(13, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

        
class TestRectangle_errors(unittest.TestCase):
    """
    tests for setter errors
    """
    def test_type_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("me")
    
    def test_type_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, "too")

    def test_type_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square( 2, 1, "like")

    def test_value_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_value_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)

    def test_value_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 1, -3)

class TestSquare_stdout(unittest.TestCase):
    """
    Unittests for testing __str__ and display methods of Square subclass
    """


    @staticmethod
    def capture_stdout(sqr, method):
        """Captures and returns text printed to stdout.
        Args:
            sqr (Square): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sqr)
        else:
            sqr.display()
        sys.stdout = sys.__stdout__
        return capture


    # Test __str__ method
    def test_str_method_print_width_height(self):
        s = Square(6)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = f"[Square] ({s.id}) 0/0 - 6\n"
        self.assertEqual(correct, capture.getvalue())


    def test_str_method_width_x(self):
        s = Square(5,1)
        correct = f"[Square] ({s.id}) 1/0 - 5"
        self.assertEqual(correct, s.__str__())


    def test_str_method_width_x_y(self):
        s = Square(8, 2, 4)
        correct = f"[Square] ({s.id}) 2/4 - 8"
        self.assertEqual(correct, str(s))


    def test_str_method_width_x_y_id(self):
        s = Square(21, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 21", str(s))


    def test_str_method_changed_attributes(self):
        s = Square(7, 0, 0, [4])
        s.width = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))


    def test_str_method_one_arg(self):
        s = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s.__str__(1)


    # Test display method
    def test_display_width(self):
        s = Square(3, 0, 0, 0)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("###\n###\n###\n", capture.getvalue())


    def test_display_width_x(self):
        s = Square(2, 1, 0, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ##\n ##\n", capture.getvalue())


    def test_display_width_y(self):
        s = Square(5, 0, 1, 0)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(display, capture.getvalue())


    def test_display_width_x_y(self):
        s = Square(4, 3, 2, 0)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(display, capture.getvalue())


    def test_display_one_arg(self):
        s = Square(1, 2, 4, 7)
        with self.assertRaises(TypeError):
            s.display(1)

class TestSquare_str_(unittest.TestCase):
    """
    Unittest for the str method
    """
    def test_str_print_width(self):
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = f"[Square] ({s.id}) 0/0 - 4\n"
        self.assertEqual(correct, capture.getvalue())


    def test_str_width_x(self):
        s = Square(5, 1)
        correct = f"[Square] ({s.id}) 1/0 - 5"
        self.assertEqual(correct, s.__str__())


    def test_str_width_x_y(self):
        s= Square(8, 2, 4)
        correct = f"[Square] ({s.id}) 2/4 - 8"
        self.assertEqual(correct, str(s))


    def test_str_width_x_y_id(self):
        s = Square(13, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 13", str(s))


    def test_str_set_attributes(self):
        s = Square(7, 0, 0, [9])
        s.width = 12
        s.x = 2
        s.y = 8
        self.assertEqual("[Square] ([9]) 2/8 - 12", str(s))


    def test_str_one_arg(self):
        s = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s.__str__(1)


class TestRectangle_update_args(unittest.TestCase):
    """
    Unittests for testing update args method of the Rectangle class
    """


    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))


    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))


    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))


    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))


    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))


    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))


    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(correct, str(s))


    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 2)
        correct = f"[Square] ({s.id}) 2/10 - 4"
        self.assertEqual(correct, str(s))


    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(3, 4, 5, 6)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))


    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")

class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
