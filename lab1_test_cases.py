import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1,2,3]), 3) # sorted list (max on right), odd length
        self.assertEqual(max_list_iter([-1,-2,-3]), -1) # negative numbers, max on the left
        self.assertEqual(max_list_iter([10,100,10]), 100)  # max in the center, and duplication
        self.assertEqual(max_list_iter([100,100,100]), 100)  # list containing identical values
         # both duplication and negative numbers in list
        self.assertEqual(max_list_iter([5,5,-9,5]), 5)
        # unsorted list, even length, duplication, and negatives
        self.assertEqual(max_list_iter([1,2,3,-6,-7,7,8,-9,-10]), 8)
        self.assertEqual(max_list_iter([1]), 0) # list with single entry
        self.assertEqual(max_list_iter([]), None) # empty list


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # basic test
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1]) # list of identical values
        self.assertEqual(reverse_rec([1,-2,3]),[3,-2,1]) # negatives
        self.assertEqual(reverse_rec([0,0,2,2,6]),[6,2,2,0,0]) # duplication in list
        self.assertEqual(reverse_rec([1]),[1]) # list with a single entry
        self.assertEqual(reverse_rec([]),[]) # empty list
    

    def test_bin_search(self):           
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 0, 0, tlist)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4) # basic test, target in center
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8) # target at right
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0) # target at left
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1) # target close to left
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None) # target not contained in list
        list_val =[0,0,0,0,0,0]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 2) # list with identical values
         # list with identical values & target not contained
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
        list_val =[-3,-2,-1,0,4]
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), 2) # list with negative values
        self.assertEqual(bin_search(-3, 0, len(list_val)-1, list_val), 0) # target negative
        list_val =[-100]
        self.assertEqual(bin_search(-100, 0, len(list_val)-1, list_val), 0) # list containing a single entry
         # list containing single entry & target not contained
        self.assertEqual(bin_search(-3, 0, len(list_val)-1, list_val), None)



        
    

if __name__ == "__main__":
        unittest.main()

    
