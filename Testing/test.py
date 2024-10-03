import unittest  # Importing the unittest module to write test cases

# A function to add two numbers
def add(a, b):
    return a + b

# A class that contains test cases for the 'add' function
class TestAddFunction(unittest.TestCase):  # Inheriting from unittest.TestCase
    
    # Test case 1: Testing the add function with positive numbers
    def test_add_positive(self):
        # Assert that add(2, 3) is equal to 5
        self.assertEqual(add(2, 3), 5)
    
    # Test case 2: Testing the add function with negative numbers
    def test_add_negative(self):
        # Assert that add(-1, -1) is equal to -2
        self.assertEqual(add(-1, -1), -2)

# This block ensures the tests run only when this script is executed directly
if __name__ == '__main__':
    # unittest.main() automatically discovers all test cases and runs them
    unittest.main()
