import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1,2,3]), 3)
        self.assertEqual(max_list_iter([-1,-2,-3]), -1)
        self.assertEqual(max_list_iter([10,100,10]), 100)
        self.assertEqual(max_list_iter([100,100,100]), 100)
        self.assertEqual(max_list_iter([5, 5, -9]), 5)
        self.assertEqual(max_list_iter([1,2,3,-6,-7,7,8,-9,-10]), 8)
        self.assertEqual(max_list_iter([]), None)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([1,-2,3]),[3,-2,1])
    

    def test_bin_search(self):           
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, tlist)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10)
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None)
        list_val =[0,0,0,0,0,0]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
        list_val =[-3,-2,-1,0,4]
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), -1)
        self.assertEqual(bin_search(-3, 0, len(list_val)-1, list_val), -3)


        
    

if __name__ == "__main__":
        unittest.main()

    
