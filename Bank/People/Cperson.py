#!usr/bin/python

from nose.tools import *
# pyimport account
"""
import NAME

This is a class representing an object person with
the following attributes
Name: The name of the person
ID: Id of the persons

"""

class person(object):

      def _init_(self,name,id):
          self._name = name
          self._id = id

      def _set_name(self,name):
          self._name = name

      def _set_id(self,id):
          self._id = id

      def _get_name(self):
          return self._name

      def _get_id(self):
             return self._id

      def _get_person(self):
            return self._name,self._id

      def _show_person(self):
            print " Name: %s, ID.:  %s " % (self._name, self._id)
