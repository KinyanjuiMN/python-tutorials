#!usr/bin/python
import sys
# sys.path.insert(0,"/Users/mac/work/projects/bank")
import People

# The import is not working! Very sad in deed.
class account(object):
      def _init_(self, person,amount):
         self._person._set_name(person._get_name)
         self._person._set_id(person._get_id)
         self._amount = amount

      def _deposit(self,person,amount):
          if self._person._get_id() == person._get_id():
              self._amount += amount
          else:
              print "The person : %s with Id: %d does not exist" % person._get_person()

      def _withdraw(self, person, amount):
          # if (self._person._get_id() == person._get_id()) and (not((self._amount- amount) < 1000))):
             self._amount -= amount


      def _get_account(self):
            return self._person, self._amount

      def _show_account(self):
             print "Name: %s, ID:%s, Balance: %d " % (self.persons._get_name(), self.person._get_id(), self._amount)
