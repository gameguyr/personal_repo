#!/usr/bin/python 

"""
Name: Therese Demers
File: address_book.py

Throughout this AddressBook class I refer to a single person as peep and to
multiple persons, or a list of persons as peeps.  Address Book contains a 
list of person objects.  In the person class I have overloaded __str__
and __eq__ so I can print and compare people easier.
"""

from person import Person
import re

class AddressBook:

  def __init__(self, peeps):
    if peeps is None:
      peeps = []
    self.people = peeps

  def addPerson(self,person):
    self.people.append(person)
  
  def findByLastName(self, lastname):
    found = AddressBook()
    lastname = lastname.lower()
    for peep in self.people:
      if lastname == peep.last.lower():
        found.addPerson(peep)
    return found

  def findByFirstName(self, firstname):
    found = AddressBook()
    firstname = firstname.lower()
    for peep in self.people:
      if firstname == peep.first.lower():
        found.addPerson(peep)
    return found

  def removePerson(self, peep):
    for thisPerson in self.people:
      if(thisPerson == peep):
        self.people.remove(thisPerson)

  def getPeople(self):
    AllPeople = []
    AllPeople.extend(self.people)
    return AllPeople
      
  def firstBeginsWith(self,prefix):
    found = AddressBook()
    for x in self.people:
      if(x.first.lower().startwith(prefix.lower())):
        found.addPerson(x)
    return found
  """ 
  Note to myself:
  You can do it all in one line:
  return AddressBook([person for person in self.people if person.first().lower()
  .startswith(prefix.lower()])
  """
  
  def findPerson(self, person):
    found = AddressBook()
    for peep in self.people:
      if person == peep:
        found.add(peep)
    return found
    
  """save() writes the contents of the address book to a file specified by the path"""  
  def save(self,path):
    with open(path,mode = 'w') as f:          #wb instead of w in windows
      for peep in self.people:
        f.write(str(peep))
        
  """load() reads from a csv file specifed by path in which the file's contents is
     a list of people, one person per line and adds the people to the address book.
     The people in the file should be entered in the following format:
     firstname, lastname, phone, street, city, state, zip, email"""      
  def load(self,path):
     with open(path, mode = "r") as f:
       for line in f:
         newPerson = re.split(',',line)
         peep = Person({'first':newPerson[0], 'last':newPerson[1], 'phone':newPerson[2], 'street':newPerson[3], 'state':newPerson[4], 'city':newPerson[5], 'zipcode':newPerson[6], 'email':newPerson[7]})
         self.addPerson(peep)
         
                      
  def lastBeginsWith(self,prefix):
      found = AddressBook()
      for x in self.people:
        if(x.last.lower().startwith(prefix.lower())):
          found.addPerson(x)
      return found
  
  def __str__(self):
      peeps = ""
      for peep in self.people:
        peeps += (str(peep) + "\n\n")
      return peeps
      
if __name__ == '__main__': 
    
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
    info2 = {'last':l,'first':f,'phone':p,'street':s,'city':c,'state':st,
            'zipcode':z,'email':e}
    jane = Person(info2)
    me = Person(info1)
    book = AddressBook([jane,me])
    print str(book)
    book.load('people.txt')
    print str(book)
    book.save('newpeople.txt')
    
    
    
