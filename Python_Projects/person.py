#!/usr/bin/python 

"""
Name: Therese Demers
File: person.py
"""

class Person(object):


  def __init__(self,kwargs):    
    for key, value in kwargs.iteritems():
      setattr(self, key, value)
    self.formatPerson()
  
  
  def formatPerson(self):
    personAttributes = ['first','last','phone','email','street','city',
    	              'state','zipcode']
    for attr in personAttributes:
      if hasattr(self,attr):
        attr = attr.title() 
        formatFunc = "format{0}".format(attr)
        func = self.__getattribute__(formatFunc)
        func()
      else:
        try:
          attr = attr.title() 
          setFunc = "set{0}".format(attr)
          func = self.__getattribute__(setFunc)
          func("None")
        except:
          #attribute is not a person attribute
          pass
  
  def formatFirst(self):
      self.first = self.first.title()
  
  def formatLast(self):
      self.last = self.last.title()

  def formatPhone(self):
      self.phone = self.phone.replace(' ','')
      self.phone = self.phone.replace('-','')
      #This handles the case if phone = 1xxxxxxxxxx
      if (self.phone[:1] == '1') and (len(self.phone) == 11):    
        self.phone = self.phone[1:]
    
  def formatCity(self):
      self.city = self.city.title()

  def formatState(self):
      self.state = self.state.upper()

  def formatStreet(self):
      self.street = self.street.title()

  def formatZipcode(self):
      pass    

  def formatEmail(self):
      pass   
 
  def setPhone(self,phone):
    if(len(phone) >= 10):
      self.phone = phone
      formatPhone(self)
    else:
      self.phone = 'None'
  
  def setFirst(self,first):
    self.first = first.title()

  def setLast(self,last):
    self.last = last.title()
    
  def setStreet(self,street):
    self.street = street.title() 
  
  def setState(self,state):
    self.state = state.upper()
        
  def setCity(self,city):
    self.city = city.title()

  def setZipcode(self,zipcode):
    self.zipcode = zipcode    
    
  def setEmail(self, email):
    self.email = email

  def fullName(self):
    return " {0} {1}".format(self.first, self.last)

  def isLongDistance(self, somePhone):
    if(len(somePhone) < 11):
      return False
    else:
      return (self.phone[:3] == somePhone[:3])

  def fullAddress(self):
    return " {0}\n {1}, {2} {3}".format(self.street, self.city, self.state, self.zipcode)

  def getPhoneNumber(self):
    if self.phone != 'None':
      return "({0}) {1}-{2}".format(self.phone[:3],self.phone[3:6],self.phone[6:10])
    else:
      return self.phone
    
  def __eq__(self, person):
    if(self.first ==person.first):
      if(self.last == person.last):  
        return True
    else:
        return False

  def __str__(self):
    return " Last Name, First Name: {0}\n Phone Number: {1}\n Address: {2} \n Email: {3}".format(self.fullName(),self.getPhoneNumber(), self.fullAddress(), self.email)

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
    print me.fullName()      
    print " " + me.phone
    print me.fullAddress()
    print str(me)
    print str(jane)
    print "Does Jane equal me?"
    print jane == me


    
      
