#!usr/bin/python
# import sys
# sys.path.insert(0,"/Users/mac/work/projects/bank")
#import People.CPerson.Person


import person

# The import is not working! Very sad in deed.
class Account(object):

      def __init__(self):
           self._member = person.Person('','')
           self._amount = 0

      def set_account(self, name, id, amount):
          self._member.set_name(name)
          self._member.set_id(id)
          self._amount = amount
      def deposit_account(self, amount):
          self._amount += amount

      def withdraw_account(self, amount):
           self._amount -= amount


      def get_account(self):
             return self._member.get_name(), self._member.get_id(), self._amount

      def get_account_name(self):
             return self._member.get_name()

      def get_account_id(self):
             return self._member.get_id()

      def get_account_balance(self):
             return self._amount

      def show_account(self):
             print "Name: %s, ID:%s, Balance: %d " % (self._member.get_name(), self._member.get_id(),self._amount)
