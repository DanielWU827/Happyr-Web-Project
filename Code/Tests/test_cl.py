'''
Unittests that test the functionality of the commandline.
All tests are self-contained and therefore require no inputs, and return no outputs.
'''
import unittest
import subprocess
from command_line import *
from ProductionCode.random_memory import *
from ProductionCode.category_helper import *
from ProductionCode.datasource import DataSource

ds = DataSource()

class TestRandom(unittest.TestCase):
    def test_get_random_memory(self):
        '''
        Test random happy memory access
        '''
        #Standard case
        memory = get_random_memory(ds)
        self.assertTrue(len(memory) > 0)
        self.assertIsInstance(memory, str)

        #Edge case with a bad ds
        bad_ds=None
        with self.assertRaises(SystemExit):
            get_random_memory(bad_ds)
    
    def test_cl_random(self):
        '''
        Test random happy memory access through command-line
        '''
        # Standard case: --random tag
        testcase = subprocess.Popen(["python3","command_line.py","--random"],stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = "utf-8")
        stdout,stderr = testcase.communicate()

        # Tests that we get a happy memory string
        self.assertIsInstance(stdout.strip(), str)


class TestRetrieveCategory(unittest.TestCase):
    def test_category(self):
        '''
        Test the function that retrieve categories
        '''
        # Standard case: call without arguments
        category_list = ["affection","achievement","enjoy_the_moment","bonding","leisure","nature","exercise"]
        for category in category_list:
            self.assertIn(category, return_categories(ds))


    def test_cl_category(self):
        '''
        Test the function that retrieve categories through commandline
        '''
        # Standard case: --category tag
        testcase = subprocess.Popen(["python3","command_line.py","--category"],stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = "utf-8")
        stdout,stderr = testcase.communicate()

        self.assertEqual(stdout.strip(),str(return_categories(ds)))

    def test_story_in_the_category(self):
        '''
        Test the story_in_the_category function
        '''
        #Standard case
        story = story_in_the_category(ds,"affection")
        self.assertTrue(len(story) > 0)
        self.assertIsInstance(story, str)

        #Edge case with an invalid input
        memory = story_in_the_category(ds, "")
        self.assertEqual(memory, "Unsupported category name, use category command to see all available categories")    

        #Edge case with bad ds
        bad_ds = None
        output = story_in_the_category(bad_ds,"affection")
        self.assertIn("Error! Something is wrong with the database:",output)    
    
    def test_cl_story_in_the_category(self):
        '''
        Test the commandline functionality of finding stories by category
        '''
        testcase = subprocess.Popen(["python3","command_line.py","--affection"],stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = "utf-8")
        stdout,stderr = testcase.communicate()

        self.assertIsInstance(stdout.strip(), str) #make sure that we get a valid string

class TestCommandLine(unittest.TestCase):
    def test_command_line_usage(self):
        '''
        Test the commandline for things that aren't covered in other tests
        '''
        testcase = subprocess.Popen(["python3","command_line.py","--help"],stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = "utf-8")
        stdout,stderr = testcase.communicate()

        # Standard Case: --help tag
        usage = "Run python3 command_line.py --category to get the list of possible categories.\n"
        usage += "Run python3 command_line.py --random to get a random happy memory!\n"
        usage += "Run python3 command_line.py --category_name to get a story in that specific category.\n"
        usage += "Run python3 command_line.py --help to get help."
        self.assertEqual(stdout.strip(),usage)

        # Edge case: meaningless tag
        testcase = subprocess.Popen(["python3","command_line.py","--foo"],stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = "utf-8")
        stdout,stderr = testcase.communicate()
        self.assertIn(usage, stdout.strip())



if __name__ == "main":
    unittest.main()
