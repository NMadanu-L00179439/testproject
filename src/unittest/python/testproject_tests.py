#from mockito import mock, verify
import unittest
from unittest.mock import Mock
import sys
import os

#data_path = os.path.join(os.path.dirname(__file__), '../src/main/python/countwords.py', 'userConfig')
sys.path.insert(0,'../src/main/python/testproject')


from testproject import userConfig

class CountWordTest(unittest.TestCase):
    def test_check_number_of_words(self):
        userConfig = Mock()
        userConfig.return_value = "Number Of Words : 5"
        out = userConfig()
        print(out)
        print('++++++++++++++++++')
        self.assertEqual(out, "Number Of Words : 4")
