'''
Unittests that test the functionality of the flask app.
All tests are self-contained and therefore require no inputs, and return no outputs.
'''

import unittest
import subprocess
from flask_app import *
from ProductionCode import random_memory
from ProductionCode import category_helper
from ProductionCode.datasource import DataSource
from ProductionCode import lookup_memory

ds = DataSource()

class TestHomepageRoute(unittest.TestCase):
    '''
    Test for the homepage route. 
    '''
    def test_homepage_route(self):
        '''
        Standard Case, Ensure homepage has the neccessary documentation.
        '''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Mission statement is only present on homepage. Use it to test routing
        mission_substring = "Our goal is to spread happiness by showing people what makes others happy!"

        self.assertIn(mission_substring, response.get_data(as_text=True))


class TestRandomRoute(unittest.TestCase):
    '''
    Test for the random route. 
    '''
    def test_random_route(self):
        '''
        Standard Case, Ensure that the random memory displayed is a string that contains text.
        '''

        self.app = app.test_client()
        response = self.app.get('/random')
        self.assertEqual(response.status_code, 200)
        memory_text = response.get_data(as_text=True).strip()
        self.assertIsInstance(memory_text, str)
        self.assertTrue(len(memory_text) > 0)
        

class TestRandomMemoryHelpers(unittest.TestCase):
    '''
    Test helper functions from random_memory.py
    '''
    def test_get_random_memory(self):
        '''
        Standard Case, Ensure get_random_memory function returns a non-empty string 
        '''
        memory = random_memory.get_random_memory(ds)
        self.assertTrue(len(memory) > 0)
        self.assertIsInstance(memory, str)

    def test_get_random_memory_bad_ds(self):
        '''
        Edge Case, Ensure bad DataSource input raises SystemExit.
        '''
        bad_ds = None
        with self.assertRaises(SystemExit):
            random_memory.get_random_memory(bad_ds)

    def test_get_random_memory_extra_param(self):
        '''
        Edge Case, Ensure extra unexpected parameters raise TypeError.
        '''
        with self.assertRaises(TypeError):
            random_memory.get_random_memory(ds, "extra")



class TestShowMemoryByIDRoute(unittest.TestCase):
    '''
    Test for the /memory/<hm_id> route
    '''
    def test_standard_cases(self):
        '''
        Standard Cases, ensure that valid memory IDs within bounds 
        return the correct memory text and a 200 status code.
        '''
        self.app = app.test_client()

        # Standard Case: the lower bound memory ID returns the correct memory
        response = self.app.get('/memory/27673')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b"I went on a successful date with someone I felt sympathy and connection with.",
            response.data
        )

        # Standard Case: the upper bound memory ID returns the correct memory
        response = self.app.get('/memory/128766')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b"I had a great workout last night.",
            response.data
        )

    def test_edge_cases(self):
        '''
        Edge Cases, ensure that invalid or out of range memory IDs 
        are handled gracefully with clear error messages and proper status codes.
        '''
        self.app = app.test_client()

        # Edge Case: ID below the minimum
        response = self.app.get('/memory/27672')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b"Invalid memory ID. Please enter an integer between 27673 and 128766, inclusive.",
            response.data
        )

        # Edge Case: ID above the maximum
        response = self.app.get('/memory/128767')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b"Invalid memory ID. Please enter an integer between 27673 and 128766, inclusive.",
            response.data
        )

        # Edge Case: non-integer ID
        response = self.app.get('/memory/abc')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            b"Invalid memory ID. Please enter an integer between 27673 and 128766, inclusive.",
            response.data
        )

class TestPageNotExist(unittest.TestCase):
    '''
    Test for the non-existent pages
    '''
    def test_error_404(self):
        '''
        Edge Case: Ensure that incorrect URL's are handled gracefully. 
        '''
        self.app = app.test_client()
        response = self.app.get('/fake_page')
        self.assertIn(b"Sorry, the page you are looking for does not exist.", response.data)

class TestCategory(unittest.TestCase):
    '''
    Test the category retrieving function
    '''
    def test_category_standard(self):
        '''
        Standard Case: Ensure that memory categories are displayed. 
        '''
        self.app = app.test_client()
        response = self.app.get('/category', follow_redirects = True)
        self.assertIn('enjoy_the_moment', response.data.decode())
        self.assertIn('leisure', response.data.decode())


class TestErrorRoutes(unittest.TestCase):
    '''
    Test for route that intentionally raises error.
    '''
    def test_internal_server_error(self):
        '''
        Edge Case, Ensure that an intentional server crash 
        returns a 500 status code as expected.
        '''
        self.app = app.test_client()
        response = self.app.get('/trigger_500')
        self.assertEqual(response.status_code, 500)


class TestLookupMemoryHelper(unittest.TestCase):
    '''
    Tests for the get_memory_text_by_id() helper in lookup_memory.py
    '''
    def test_standard_lower_bound(self):
        '''
        Standard Case, Ensure a valid lower-bound ID returns non-empty text (not None).
        '''
        result = lookup_memory.get_memory_text_by_id(ds, 27673)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result.strip()) > 0)

    def test_standard_upper_bound(self):
        '''
        Standard Case, Ensure a valid upper-bound ID returns non-empty text (not None).
        '''
        result = lookup_memory.get_memory_text_by_id(ds, 128766)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result.strip()) > 0)

    def test_not_found_id(self):
        '''
        Edge Case, Ensure a non-existent ID returns None (no crash).
        '''
        result = lookup_memory.get_memory_text_by_id(ds, 999999999)
        self.assertIsNone(result)

    def test_non_integer_id(self):
        '''
        Edge Case, Ensure a non-integer ID input is handled gracefully and returns None.
        '''
        result = lookup_memory.get_memory_text_by_id(ds, "abc")
        self.assertIsNone(result)

    def test_none_id(self):
        '''
        Edge Case, Ensure None as ID returns None without raising an exception.
        '''
        result = lookup_memory.get_memory_text_by_id(ds, None)
        self.assertIsNone(result)

    def test_bad_ds_param(self):
        '''
        Edge Case, Ensure a bad DataSource parameter raises AttributeError (no .connection).
        '''
        bad_ds = None
        with self.assertRaises(AttributeError):
            lookup_memory.get_memory_text_by_id(bad_ds, 27673)



if __name__ == '__main__':
    unittest.main()