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
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number, get_amount, get_balance

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

    def test_get_amount_raise_exception_numeric(self):
        # Arrange
        user_input = "Not Numeric"

        #Act
        # Mock the user_input and return as user_input
        # catches TypeError.
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(TypeError) as e:
                get_amount()
            

        # Assert
        # compare the two if they match
        expected_message = "Amount must be a numeric type."
        self.assertEqual(str(e.exception), expected_message)

    def test_get_amount_raise_exception_zero_value(self):
        # Arrange
        user_input = 0

        # Act
        # Mock the user_input and return as user_input 
        # Raise ValueError
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(ValueError) as e:
                get_amount()

        # Assert
        # compare the two if they match
        expected_message = "Amount must be a value greater than zero."
        self.assertEqual(str(e.exception), expected_message)
        
    def test_get_amount_raise_exception_less_than_zero_value(self):
        # Arrange
        user_input = -1

        #Act
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(ValueError) as e:
                get_amount()

        # Assert
        # compare the two if they match
        expected_message = "Amount must be a value greater than zero."
        self.assertEqual(str(e.exception), expected_message)

    def test_get_amount_returns_valid_amount(self):
        # Arrange
        user_input = 1

        # Act
        with patch('builtins.input', return_value = user_input):
            valid_amount = get_amount()

        # Assert
        # Almost equal can accept int and float
        # It is identically almost the same
        # compare the two if they match with valid_amount
        self.assertAlmostEqual(valid_amount, 1)

    def test_get_balance_raise_exception_not_integer_type(self):
        # Arrange
        user_input = "Not an int"

        # Act
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(TypeError) as e:
                get_balance(user_input)
            
        # Assert
        expected_message = "Account number must be an int type."
        self.assertEqual(str(e.exception), expected_message)

    def test_get_balance_raise_exception_not_valid_account(self):
        # Arrange
        user_input = 12345

        # Act
        with patch('builtins.input', return_value = user_input):
            with self.assertRaises(ValueError) as e:
                get_account_number()

        # Assert
        expected_message = "Account number entered does not exist."
        self.assertEqual(str(e.exception), expected_message)

    
if __name__ == "main":
    main()