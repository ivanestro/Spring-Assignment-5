# Assignment 5

In this assignment, you will have the opportunity to practice your knowledge of Python functions by creating a chatbot that assists customers with banking tasks. Prior to this assignment, you will have learned about git, variables and data types, exception handling, looping and data structures. By completing this assignment, you will learn valuable skills that are essential for a professional software developer such as code organization, modularity, and best practices for developing functions and corresponding unit tests.

## Author

Ivan Estropigan

## Requirements

**UserStory**
As a banking customer,

I want to check my account balance and make deposits,

So that I can keep track of my finances and make transactions easily.

## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions

- The ValueError and raise TypeError figuring out how I can implement this code.

- For unit test I have issues trying to run the code as to what I should put if I am dealing with exception messages the self.assertEquals(str()) function. I had to re-look into the powerpoint/learning_module_5_part_2.

- In the Test file, I have used the self.assertAlmostEqual function basically it is to compare both values as either int or float that is at most almost equal.

- src chatbot.py get_balance working with type error, value error exception as a return recalling function along with the error message. This gave me a lot of errors trying to figure out whats wrong with the try and exception.

### 2. Discuss the benefits and challenges of developing and using unit tests

- The benefit of developing unit test is to make sure that we capture bugs early on and time management to help lessen the time to figure out what went wrong rather than using the old one by one debugging.
-
-

## Code Modification 1

- Modified: Author name, Version, Credits

- Added: user_number for users to interact what their account is.
- Added: Defining get_account to validate if the user interacts with the correct dictionary.
- Added: Raise TypeError and ValueError if user inputs wrong account either string/int not in dictionary.

## Code Modification 2

- Modified: Author, Version, Credits

- Added: get_account_number to the from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number
- Added: class TestChatBot(TestCase):
- Added: defined each specific test_get_account to their desired functions of what they do. Such as:
TypeError, ValueError, Matching Valid Account.

## Code Modification 3

- Deleted: while loop, this assignment is only test purposes not running an app program :c

- Modified: Fixes Indentation from while loop:

## Code Modification 4

- Modified: doc string messages to chatbot.py such as Description, Args, Return, Raise etc.

- Added: Test get_amount in src chatbot.py if the amount is entered in alphabets typeError is raised. If the value is entered less than
0 ValueError occurs.
- Added: test_chatbot.py testing all the raise exceptions from the src chatbot.py to simulate the errors and to check the changes.
- Added: README Struggles with a new self.assertAlmostEqual function.

## Code Modification 5

- Added: src chatbot.py get_balance() so that customer are able to get their balance from account ID with the message.
- Saving and Commiting - Update soon for Unit Testing.
[EOF]