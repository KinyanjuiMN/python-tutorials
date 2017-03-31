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

class Person(object):

      def __init__(self, name, id):
          self._name = name
          self._id = id


      def set_name(self,name):
          self._name = name

      def set_id(self,id):
          self._id = id

      def get_name(self):
          return self._name

      def get_id(self):
          return self._id

      def get_person(self):
          return self._name,self._id

      def show_person(self):
          print " Name: %s, ID.:  %s " % (self._name, self._id)
