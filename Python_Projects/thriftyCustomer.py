#!/usr/bin/python

"""
  Author: Therese Demers
  File: thriftyCustomer.py

""" 

"""
  ThriftyCustomer extends the Person class
  Thrifty Customer has 3 added attributes:
  accountNumber, balance and socialSecurity
"""

from person import Person

class ThriftyCustomer(Person,object):
  
  def __init__(self,kwargs):
    Person.__init__(self,kwargs)

  def setAccountNumber(self,number):
    self.accountNumber = number

  def setBalance(self,amount):
    self.balance += amount

  def setSocialSecurity(self,ss):
    self.socialSecurity = ss

  def getAccountNumber(self):
    return self.accountNumber

  def getBalance(self):
    return self.balance

  def getSocialSecurity(self):
    return self.socialSecurity
    
  def __eq__(self,customer):
    if (self.accountNumber == customer.accountNumber):
      if (self.socialSecurity == customer.socialSecurity):
        return True
    else:
       return False

  def __str__(self):
    customerString= "first:{0},last:{1},phone:{2},street:{3},city:{4},state:{5},zipcode:{6},email:{7},accountNumber:{8},balance:{9},socialSecurity:{10}".format(self.first,self.last,self.phone, self.street,self.city, self.state, self.zipcode,self.email, self.accountNumber, self.balance, self.socialSecurity)
    return customerString

if __name__ == "__main__":
    customer1 = {'first':'Therese','last':'Demers','phone':'415 797 3434',
            'street': '1 Something St.','city':'San Francisco','state':'ca',
            'email':'blah@gmail.com', 'accountNumber': '123456', 
            'socialSecurity': '1111111111','balance': '4' }
    customer2 = {'first':'Jane','last':'Doe','phone':'415 797 3333',
            'street': '1 Something St.','city':'San Francisco','state':'ca',
            'email':'dummy@yahoo.com', 'accountNumber': '123456', 
            'socialSecurity': '1111111111','balance': '4'}

    me = ThriftyCustomer(customer1)
    jane = ThriftyCustomer(customer2)
    print jane
    print "Does my account equal jane's account?"
    print me == jane


