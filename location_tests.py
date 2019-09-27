import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")
        loc = Location("Brisbane", -27.5, 153.0)
        self.assertEqual(repr(loc),"Location('Brisbane', -27.5, 153.0)")
    
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1 == loc2, True)
        loc1 = Location("Brisbane", -27.5, 153.0)
        loc2 = Location("Brisbane", -27.5, 153.0)
        self.assertEqual(loc1 == loc2, True)
        loc1 = Location("Brisbane", -27.5, 153.0)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1 == loc2, False)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
