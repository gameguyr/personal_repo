#!/usr/bin/python

"""
Author: Therese Demers
File: thriftyBank.py
"""

from __future__ import division
from thriftyCustomer import *
import sys
import random
import re


"""
When ThriftyBank is opened/executed the database, or a dictionary, 
is initialized to the stored values in the file CustomerDB.txt.
From this file the database, currentCustomers, is initialized to
ThriftyBank customers with the account number as the key.
When the bank is closed/execution is stopped, all the transactions
that happened is dumped into the external file, CustomerDB.txt
"""

class ThriftyBank(ThriftyCustomer):

  def __init__(self):
    self.currentCustomers = dict()     #dictionary contains ThriftyCustomers
    self.initializeCustomerDatabase()


  """
  newCustomer() prompts, retrieves and validates new customer information and then adds the
  customer to the customer database, or, currentCustomers
  """
  def newCustomer(self):
    customerInput = ['First Name:','Last Name:','Address-\nStreet: ','City: ','State: ','Zip Code: ','Phone (with area code): ','Email: ']
    databaseFields = ['first','last','street','city','state','zipcode','phone','email']
    tempCust = {}   # To temporarily store values customer enters before adding customer to database
    isAccountNumValid = False
    isSSValid = False
    inputValue = 'N'
    """
    The following loop prompts the new customer to enter each xth value
    in the customerInput list and then appends the value entered with 
    xth value in the databaseFields list as the key to the tempCust dictionary.
    """
    print "Please enter the following information for your new account:"
    x = 0
    for v in customerInput:
      while(inputValue == 'N'):
        value = raw_input(customerInput[x])
        print "You entered: " + value
        inputValue = raw_input("Is this correct? (Y or N)")
        inputValue.upper()
      tempCust[databaseFields[x]] = value
      x = x + 1
      inputValue = 'N'

    """
    The following is to prompt the user for their Social Security Number 
    and then validates that it is indeed valid.
    """
    while isSSValid == False:
      while(inputValue == 'N'):
        socialSecurity = raw_input("Social Security Number:")
        print "You entered: " + socialSecurity
        inputValue = raw_input("Is this correct? (Y or N)")
        inputValue.upper()
      isSSValid = self.validateSocialSecurity(socialSecurity)
      if isSSValid == False:
        inputValue = 'N'
        print "The social security number entered is invalid. Please reenter.\n"
      else:
       tempCust['socialSecurity'] = socialSecurity

    """
    The following generates an account number of 10 digits long that
    is a random integer between 1 and the max int, then validates
    that the account number generated is valid.
    """
    while isAccountNumValid == False:
      accountNumber = '{0:10}'.format(random.randint(1,sys.maxint))  
      accountNumber = accountNumber.replace(' ', '')     # In case the account number is less than 10 digits
      isAccountNumValid = self.validateAccountNumber(accountNumber)
      if isAccountNumValid:
        tempCust['accountNumber'] = accountNumber

    tempCust['balance'] = int(0)    #initialize new customer's balance to 0
    # The following creates and adds the customer to the database
    customer = ThriftyCustomer(tempCust)    
    self.currentCustomers[accountNumber] = customer
    print "Congratulations {0}, you are now a customer of Thrifty Bank!\n".format(customer.fullName())
    print "Please take note of your account number: {0}".format(accountNumber)
    raw_input("Press ENTER to return to the main menu.")
  
  """
  loseCustomer() is called when the customer wants to close their account.
  """
  def loseCustomer(self):
    customerAccount = raw_input("Please enter your account number: ")
    del self.currentCustomers[str(customerAccount)]

  """
  transaction() calls the makeDeposit, makeWithdrawal or getBalance functions,
  depending on the user input.  It also validates that the user's input is valid.
  """
  def transaction(self):
   #The following is for debugging
   # for key, value in self.currentCustomers.iteritems():
     # print str(key)
     # print type(key)
     # print str(value) 
     # print type(value)

    transactionTypes = ['makeDeposit','makeWithdrawal','getBalance']
    acctNumber = raw_input("Please enter your account number: ")
    acctNumber = str(acctNumber)
    if acctNumber in self.currentCustomers:
      customer = self.currentCustomers.get(acctNumber)
    else:
      print "The account number entered does not exist.  Returning to main menu."
      return 0
    isTransaction = False
    while(isTransaction == False):
      print "Welcome back {0}!".format(customer.fullName())
      print "Please select from one of the following choices: \n"
      print "1: Make a deposit\n2: Make a withdrawal\n3: Get current balance\n"
      selection = raw_input("Enter selection (1-3): ")
      selection = int(selection)
      try:
        transFunc = transactionTypes[selection-1]
        func = self.__getattribute__(transFunc)
        func(customer)
        isTransaction = True
      except:
        print "Invalid selection.  Please make a valid selection.\n"

    print "Thrifty Bank appreciates your business!"

  """
  makeDeposit() receives an amount to deposit from the customer, rounds 
  the amount to the dollar and donates the cents to Thrifty employees,
  I mean, children in Africa.  It verifies that the amount user entered
  is a valid entry.
  """
  def makeDeposit(self,customer):
    print "Please note that all deposits that contain cents,"
    print "Thrifty Bank automatically rounds the deposit amount to whole"
    print "dollars and donates the change to the starving children in Ethiopia."
    print "If you have a problem with helping out the needy, you can do your"
    print "banking some where else."
    custInput = raw_input("Please enter deposit amount: ")
    custInput = float(custInput)
    deposit = custInput//1  #To turn deposit into whole numbers
    donation = custInput - deposit
    if donation > 0:
       print "Thank you for donating {0} cents to the starving children of Ethiopia!\n".format(donation)
    if self.validateAmount(deposit) == False:
      print "Your deposit is invalid.  Please try again later!\n"
    else:
      deposit = int(deposit)
      accountNum = customer.getAccountNumber()
      customer.setBalance(deposit)
      currbalance = customer.getBalance()
      print "Your new balance is: {0}\n".format(currbalance)
      self.currentCustomers[accountNum] = customer  # To update the database with this transaction
  
  """
  makeWithdrawal() receives an amount to withdraw, validates that
  amount entered is valid and then deducts the withdrawal amount from
  the customer's account. 
  """
  def makeWithdrawal(self,customer):
    amount = raw_input("Please enter withdrawal amount: ")
    amount = int(amount)
    if self.validateWithdrawal(customer,amount) == False or self.validateAmount(amount) == False:
      print "The withdrawal amount is invalid.  Please try again later!\n"
    else:
      if amount > 0:
        amount = amount * -1
      accountNum = customer.getAccountNumber()
      customer.setBalance(amount) 
      print "Your new balance is: {0}\n".format(customer.getBalance())
      self.currentCustomers[accountNum] = customer

  """
  getBalance() gets the balance from the customer and prints it to the screen.
  """
  def getBalance(self,customer):
    balance = customer.getBalance()
    print "Your current balance is: {0}\n".format(balance)
  
  """
  validateAccountNumber() makes sure that the newAccountNumber is already
  being used by another customer.
  """
  def validateAccountNumber(self,newAccountNumber): 
    isValid = True 
    for account,customer in self.currentCustomers.iteritems():
      if account == newAccountNumber:
        isValid = False
    return isValid

  """
  validateSocialSecurity() removes any hyphens or spaces that the user
  may have entered and makes sure that no letters were entered and that
  the social security number is equal to 9 digits.
  """
  def validateSocialSecurity(self,ss):
    ss = ss.replace('-','')
    ss = ss.replace(' ','')
    if len(ss) != 9 or ss.isalpha():
      return False
    else:
      return True

  """
  validateWithdrawal() makes sure that the amount the user entered
  to withdraw is less than or equal to the balance of the customer
  account.  If there is enough money to be withdrawn it will return True
  else it will return false.
  """
  def validateWithdrawal(self,customer,amount):
    balance = customer.getBalance()
    if amount > 0:
      amount = amount * -1
    if (balance + amount) >= 0:
      return True
    else:
      return False

  """
  validateAmount() ensures that the amount is greater than or equal to
  0 and that it is less than the maximum int .
  """
  def validateAmount(self, amount):
    if amount <= 0 or amount >= sys.maxint:
      return False
    else:
      return True
    
  def validateCustomer():
    pass
 
  """
  initializeCustomerDatabase() opens the file CustomerDB.txt that contains
  a list of customers and initializes the current customer database, or
  currentCustomers dictionary, to the list of customers in CustomerDB.
  CustomerDB has the customers as strings so it is parsed and turned into
  a customer ThriftyCustomer object and then added to the currentCustomers.
  """
  def initializeCustomerDatabase(self):
    rf = open("CustomerDB.txt")
    temp = rf.readlines()
    for line in temp:
      try:
        customer = {}           # Customer is a temporary dictionary that is used to store the values, attributes for each customer
        line.strip()
        line.rstrip('\n')
        nextLine = re.split(',',line)  # Creates a list of customer attributes, ie [first:Therese,last:Demers....]
        for x in nextLine:      # For attribute in list of customer attributes
          x.strip()             # Get rid of white space
          y = re.split(':',x)   # Create another list, or tuple, [Attribute Name, Value], ie [first,Therese]
          attr = y[0]           # y[0] = Attribute Name (ie first)
          if attr == 'balance': # If the attribute name is balance, turn the value into an int.
            y[1] = int(y[1])        
          value = y[1]          # Value is the stored value of the attribute (ie Therese)
          customer[attr] = value  # Add the attribute and value to the customer dictionary, attribute is the key
        customer = ThriftyCustomer(customer)  # After all the attributes and values have been read and parsed from the file,
                                              # create a Thrifty Customer using the values stored in the customer dictionary.
        account = customer.getAccountNumber()  # Retrieve the customer's account number
        self.currentCustomers[account] = customer  # Add the Thrifty Customer to the currentCustomer, with account number as key
      except:
        "Problem initializing customer database."
    rf.close()

  def getCustomerDatabase(self):
    return self.currentCustomers
 
  """
  Before this program exits, it will write the current customers information
  to the CustomerDB.txt file to store all the new customers, transactions that
  occured.
  """
  def dumpCustomerDatabase(self):
    f = "CustomerDB.txt"
    rf = open(f,"w")
    for account,customer in self.currentCustomers.iteritems():
      rf.write(str(customer)+'\n')
    rf.close()
   
  def printMainMenu(self):
    print "\nWelcome to Shifty, I mean, Thrifty Bank!\n"
    print "Please select from one of the following options:\n"
    print "1: Make a withdrawal/deposit/check balance"
    print "2: Open a new account with Thrifty Bank."
    print "3: Close your current account with Thrifty Bank."
    print "4: To exit the system."

if __name__ == "__main__":
  
    bank = ThriftyBank()  
    mainSelections = ['transaction','newCustomer','loseCustomer']    
    session = True
    while session == True:
      bank.printMainMenu()
      selection = raw_input("Enter your selection (1-4): ")
      if int(selection) == 4:
        bank.dumpCustomerDatabase()
        session = False
        print "Thrifty Bank thanks you for your business! Come again!"        
      elif int(selection) < 1 or int(selection) > 4:
        print "You did not enter a valid selection, please try again."
      else:
        mainFunc = mainSelections[int(selection)-1]
        func = bank.__getattribute__(mainFunc)
        func()

    

