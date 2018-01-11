#!/usr/bin/python

from __future__ import print_function
from flask import Flask, request
from address_book import AddressBook
from person import Person


app = Flask('addressbook')
book = AddressBook()
book.load("newpeople.txt")

@app.route('/')
def index():
  page = "This is my address book\n"
  for person in book:
    page += "{1},{0}: {2}\n".format(person.first(), person.last(), person.phone())
  return page

@app.route('/browse/<letter>'):
def browse(letter):
  pass

app.run()


