"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number

__author__ = "Ivan Estropigan"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty, W3School, FreeCodeCamp, pylint.readthedocs.io"

class TestChatBot(TestCase):
    
    
    def test_get_account_number_raises_type_error(self):
        # Arrange
        user_input = "non_numeric_data" # Checking when user_input as test

        # Act
        # Mock the input function to return "non_numeric_data"
        # To simulate user_input
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(TypeError)as e:
                get_account_number()
        
        # Assert
        # Exception Message
        # str is to handle string messages
        # exception for errors
        expected_message = "Account number must be an int type."
        self.assertEqual(str(e.exception), expected_message)

    def test_get_account_number_raises_value_error(self):
        # Arrange
        user_input = "112233"

        # Act
        # mock the input function to return "112233"
        # Simulating user_input
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(ValueError)as e:
                get_account_number()
        
        # Assert
        # Exception Message as expected_message
        # str is to handle string messages
        # exception for errors
        expected_message = "Account number entered does not exist."
        self.assertEqual(str(e.exception), expected_message)

    
    def test_get_account_number_verify_valid_account(self):
        # Arrange
        user_input = "123456"
        expected_account = 123456

        # Act
        # mock the user_input to return 123456
        # return the user_input 123456
        with patch('builtins.input', return_value = user_input):
                account_123456 = get_account_number()

        # Assert
        # does the account number equals?
        # if so ok if not error
        self.assertEqual(account_123456, expected_account)

if __name__ == "main":
    main()