import unittest
from src import rectangle, circle, triangle, trapezoid, sphere

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = rectangle.perimeter(5, 10)
        self.assertEqual(res, 30)


class CircleTestCase(unittest.TestCase):
    def test_area_unit(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.141592653589793)

    def test_perimeter(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 12.566370614359172)


class TriangleTestCase(unittest.TestCase):
    def test_area_geron(self):
        res = triangle.area(3, 4, 5)
        self.assertEqual(res, 6.0)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle.area(1, 2, 10)


class TrapezoidTestCase(unittest.TestCase):
    def test_area(self):
        res = trapezoid.area(4, 6, 4)
        self.assertEqual(res, 20.0)

    def test_perimeter(self):
        res = trapezoid.perimeter(4, 6, 5, 5)
        self.assertEqual(res, 20)


class SphereTestCase(unittest.TestCase):
    def test_volume(self):
        res = sphere.volume(0)
        self.assertEqual(res, 0)

    def test_surface_area(self):
        res = sphere.surface_area(1)
        self.assertAlmostEqual(res, 12.566370614359172)


if __name__ == "__main__":
    unittest.main()