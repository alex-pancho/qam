import unittest
import task_03

class TaskTest(unittest.TestCase):

    def test_for_triangels_positive_tri(self):
        check_result = task_03.is_triangles(2,2,2)
        self.assertEqual("is triangle", check_result)
    
    def test_for_triangels_positive_not_tri(self):
        check_result = task_03.is_triangles(2,2,22)
        self.assertEqual("is not", check_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)