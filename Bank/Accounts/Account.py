#!usr/bin/python
# import sys
# sys.path.insert(0,"/Users/mac/work/projects/bank")
#import People.CPerson.Person
import os
from ..people import Person

# The import is not working! Very sad in deed.
class account(object):
      def _init_(self, Person,amount):
         self._Person._set_name(Person._get_name)
         self._Person._set_id(Person._get_id)
         self._amount = amount

      def _deposit(self,Person,amount):
          if self._Person._get_id() == Person._get_id():
              self._amount += amount
          else:
              print "The Person : %s with Id: %d does not exist" % Person._get_Person()

      def _withdraw(self, Person, amount):
          # if (self._Person._get_id() == Person._get_id()) and (not((self._amount- amount) < 1000))):
             self._amount -= amount


      def _get_account(self):
            return self._Person, self._amount

      def _show_account(self):
             print "Name: %s, ID:%s, Balance: %d " % (self.Persons._get_name(), self.Person._get_id(), self._amount)
