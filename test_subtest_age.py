import unittest
from age import categorize_by_age

class TestAgeSubtest(unittest.TestCase):

    def test_child(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                
                print(f"{age} is considered as a child")   
                
                self.assertEqual(result, "Child")

if __name__ == "__main__":
    unittest.main(verbosity=2)