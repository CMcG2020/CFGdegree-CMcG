'''Simple ATM program
Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money.
(NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
Tasks:
1.       Prompt user for a pin code
2.       If the pin code is correct then proceed to the next step, 
        otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.
3.       Set account balance to 100.
4.       Now we need to simulate cash withdrawal
5.       Accept the withdrawal amount
6.       Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
7.       However, when a user asks to ‘withdraw’ more money than they have on their account, 
        then you need to raise an error an exit the program. 
'''
#Check for valid pin.
def verify_pin(pin):
    return pin == 1111

#Give user three attempts to try pin
def log_in():
    tries = 0
    while tries < 3:
        pin =int(input('Please Enter Your 4 Digit Pin: '))
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False


def check_input(withdraw):
    try:
        withdraw = int(withdraw) # check if input is a number
        try:
            if withdraw <= 0: # check if withdraw is negative
                raise ValueError("Please enter a valid amount. ")
        except ValueError as ve:
            print (ve)
            return False
    except ValueError:
        print("Invalid input")
        return False
    else:
        return True


# transaction function to withdraw money
def transaction(withdraw):
    balance = 100 ##set account balance to 100
    try:
        x = balance - withdraw
        if x < 0: # check if balance is negative
            raise ValueError("Insufficient fund!")
    except ValueError as ve:
        print(ve)
    else:
        balance -= withdraw  # subtract withdraw from balance 
        print(f"Your balance is: £{balance}.")
    return balance
def main():
    if log_in():
        withdraw = (input('please enter withdrawal amount: '))
        if check_input(withdraw):
            transaction(int(withdraw))

main()

'''ATM test file'''

from unittest import TestCase, mock
import unittest

from hw_4 import verify_pin, check_input, transaction
#import locally functions to test

class ATM_test(unittest.TestCase):

#1.test withdrawl works
    def test_correct_withdrawal(self):
        result = transaction(withdraw=20)
        self.assertEqual(result, 80)


#2.test if withdrawal doesn't not work
    def test_incorrect_withdrawal(self):
        result = transaction(withdraw=350)
        self.assertEqual(result, 100)


#3.check correct pin is recognised
    def test_correct_pin(self):
        a = verify_pin(pin=1111)
        self.assertTrue(a)


#4.test if incorrect pin is recognised
    def test_incorrect_pin(self):
        a = verify_pin(pin=1234)
        self.assertEqual(a, False)

    
#5.test if input is a number
    def test_input_is_number(self):
        a = check_input(withdraw="a")
        self.assertEqual(a, False)

#6.test if input is a negative number
    def test_input_is_negative(self):
        a = check_input(withdraw=-20)
        self.assertEqual(a, False)

#7.test if input is a positive number
    def test_input_is_positive(self):
        a = check_input(withdraw=20)
        self.assertEqual(a, True)
    
#8.test if input is a zero
    def test_input_is_zero(self):
        a = check_input(withdraw=0)
        self.assertEqual(a, False)

# -- unit test --

if __name__ == '__main__':
    unittest.main(verbosity= 2)



