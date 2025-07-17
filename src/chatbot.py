"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "Ivan Estropigan"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty, W3School,freeCodeCamp, pylint.readthedocs.io"


ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]


def chatbot():
    """
    Description:
        Performs the Chatbot functionality."""
    
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

def get_account_number() -> int:
    """
    Description:
        User interaction verifies an account number in a loop

    This validates the user that they enter an account number correctly
    if not check in ACCOUNTS if it exists in the dictionary.

    Args:
        None

    Returns:
        int: To Validate account number

    Raises:
        TypeError: This raises an exception if the user input is a string
        ValueError: This raises an exception if the user input does not exist
        in the dictionary.
    
    Otherwise accept the account
    """

    user_number = input("Please enter your account number: ")

    try:
        account_number = int(user_number)
        
    except ValueError as e:
        raise TypeError("Account number must be an int type.") from e
        
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
        
    # If user did input correct account information
    # return the account number.
    if account_number in ACCOUNTS:
        return account_number
        
def get_amount() -> float:
    """
    Description:
        prompts the user to input the amount deposit and return the value as a float

    Args:
        None

    Return:
        float: get the valid amount and return as float

    Raise:
        TypeError: Input must be a numeric type. 
        ValueError: If user input is 0 or less than tell the user that it should be greater than zero.

    Otherwise anything greater than 0 should return the amount without any exceptions being raised.
    """
    user_add_input = input("Enter an amount: ")

    try:
        amount = float(user_add_input)
    
    except ValueError as e:
        raise TypeError("Amount must be a numeric type.") from e
    
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    return amount
    

if __name__ == "__main__":
    chatbot()


