#!/usr/bin/python

"""
Author: Therese Demers
File: bankRobbers.py
"""
 
"""
This is an inside job.  You know some one that works for Thrifty Bank and 
has all the codes to get into the bank's internal network.
"""

print "Today's mission is to break into Thrifty Bank,"
print "\n withdraw all the money from every current customer and\n"
print "then delete the customer database using only strings.\n"

targetBankString = "Thrifty Bank"
targetBankString = targetBankString.replace(' ','')
targetBank = targetBankString[0].lower() + targetBankString[1:]

openBank = __import__(targetBank)  # openBank is a module of type thriftyBank.py 
bankModules = dir(openBank)  # So I know what modules are included in the file thriftyBank.py
print dir(openBank)
bank = getattr(openBank,targetBankString)  # bank is now an object of type ThriftyBank

funcs = dir(bank)  # So I know what functions are in the ThriftyBank that I can use
print dir(bank)
newBank = bank()   # newBank is now an instance of Thrifty Bank

getDBfunc = getattr(bank,"getCustomerDatabase")  # getDBfunc is now a function of type getCustomerDatabase  

customerDB = getDBfunc(newBank)  # customerDB is now a database of Thrifty Bank customers and account numbers
print customerDB
customerAccountNumbers = customerDB.keys()  # List of customer account numbers

customers = customerDB.values()  # List of current Thrifty Bank customers

customerBalances = {}

for customer in customers:
  balance = customer.getBalance()       # Retrieving all the balances from all the customers' accounts
  customerBalances[customer] = balance  # and storing them in a dictionary with customer as the key

withdraw = getattr(bank,"makeWithdrawal")  # withdraw is now a function of type makeWithdrawal 
robbersBankAccount = int(0)                # robbers' bank account is currently zero
for customer in customerBalances:               
  withdrawalAmount = customerBalances[customer]  # withdrawalAmount is the balance of the customer's account
  print withdrawalAmount                         # print the amount to the screen so the robber can enter
                                                 # the amount in for the withdrawal prompt
  withdraw(newBank,customer)                     # The customer's balance is now zero
  robbersBankAccount = robbersBankAccount + int(withdrawalAmount)  # Robber deposits the withdrawed amount to his/her bank account/pocket

del newBank.currentCustomers                   # All current customers are now deleted from the bank
dumpDB = getattr(bank,"dumpCustomerDatabase")  # dumpDB is now a function of type dumpCustomerDatabase 
try: 
  newBank.dumpCustomerDatabase()               # Updating the database to now reflect that there are no customers
                                               # This will throw an error because there are no current customers
except:                                        # So the database is now empty and we caught the exception so that
  pass                                         # the authorities won't find out until they try to access the database again.
print "Mission accomplished!  Database has been deleted completely and we now have {0} in our bank account!".format(robbersBankAccount)
