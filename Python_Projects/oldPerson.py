#!/usr/bin/python 

"""
Name: Therese Demers
File: person.py

A person can have a first name, last name, phone number (entered as just numbers),
street, city, state, zipcode and email.
"""

class Person(object):

  def __init__(self,kwargs):    
    for key, value in kwargs.iteritems():
      setattr(self, key, value)
    self.formatPerson()
  
  def formatPerson(self):
    if hasattr(self,'first'):    
      f = self.first
      self.first = f.title()
    else:
      self.first = 'None'
    if hasattr(self, 'last'):
      f = self.last
      self.last = f.title()
    else:
      self.last = 'None'
    if hasattr(self, 'phone'):
      f = self.phone
      self.phone = f.replace(' ','')
      #This handles the case if phone = 1xxxxxxxxxx
      if (f[:1] == '1') and (len(f) == 11):    
        f = f[1:]
        self.phone = f      
    else:
      self.phone = 'None'
    if hasattr(self, 'city'):
      f = self.city
      self.city = f.title()
    else:
      self.city = 'None'
    if hasattr(self, 'state'):
      f = self.state
      self.state = f.upper()
    else:
      self.state = 'None'
    if hasattr(self, 'street'):
      f = self.street
      self.street = f.title()
    else:
      self.street = 'None'
    if hasattr(self, 'zipcode') == False:
      self.zipcode = 'None'
    if hasattr(self, 'email') == False:
      self.email = 'None'
      
  def full_name(self):
    return " {0}, {1}".format(self.last, self.first)

  def isLongDistance(self, somePhone):
    if(len(somePhone) < 11):
      return False
    else:
      return (self.phone[:3] == somePhone[:3])

  def SetPhoneNumber(self,phone):
    if(len(phone) >= 11):
      if phone[:1] == 1:    #This handles the case if phone = 1 415....
        tempphone = phone[1:]
        phone = tempphone
      self.phone = phone.replace(' ','')
    else:
      self.phone = 'None'
  
  def SetFirstName(self,first):
    self.first = first.title()

  def SetLastName(self,last):
    self.last = last.title()
    
  def SetStreet(self,street):
    self.street = street.title() 
  
  def SetState(self,state):
    self.state = state.upper()
        
  def SetCity(self,city):
    self.city = city.title()

  def SetZip(self,zipcode):
    self.zipcode = zipcode    
    
  def full_address(self):
    return " {0}\n {1}, {2} {3}".format(self.street, self.city, self.state, self.zipcode)

  def phone_number(self):
    if self.phone != 'None':
      return "({0}) {1}-{2}".format(self.phone[:3],self.phone[3:6],self.phone[6:10])
    else:
      return self.phone
      
  def SetEmail(self, email):
    self.email = email
    
  def __eq__(self, person):
    if(self.first ==person.first):
      if(self.last == person.last):  
        return True
    else:
        return False

  def __str__(self):
    return " Last Name, First Name: {0}\n Phone Number: {1}\n Address: {2} \n Email: {3}".format(self.full_name(),self.phone_number(), self.full_address(), self.email)

if __name__ == "__main__":
  
    l = 'Doe'
    f = 'Jane'
    p = '1 415 799 4343'
    s = '5 Nowhere St.'
    c = 'Boondocks'
    st = 'tx'
    z = '23102'
    e = 'duh@yahoo.com'
    info1 = {'first':'Therese','last':'Demers','phone':'415 797 3434',
            'street': '1 Something St.','city':'San Francisco','state':'ca',
            'email':'blah@gmail.com'}
    info2 = {'last':l,'first':f,'phone':p,'street':s,'city':c,'state':st,'zipcode':z,'email':e}
    jane = Person(info2)
    me = Person(info1)
    print me.full_name()      
    print " " + me.phone
    print me.full_address()
    print str(me)
    print str(jane)
    print "Does Jane equal me?"
    print jane == me


    
      
