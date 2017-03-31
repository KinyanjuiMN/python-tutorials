# import pdb
import account


class members(object):
      """ The members class  keeps a list of members of the bank """

      def __init__(self):
          self._list_of_members = {}

      def  get_member_account(self):
           return self._member_account


      def _add_member(self,name,id,amount):
          self._account =account.Account()
          if self._list_of_members.has_key(id) == False:
              self._account.set_account(name,id,amount)
              dict = {id:self._account }
              self._list_of_members.update(dict)
          else:
              print "The member:  %s with Id: %s already exists \n" % (name,id)

      def _deposit_member_account(self,name,id,amount):
           # pdb.set_trace()
           if self._list_of_members.has_key(id):
              self. _list_of_members.get(id,'none').deposit_account(amount)
              dict = {id:self. _list_of_members.get(id,'none')}
              self._list_of_members.update(dict)
           else:
               print "No deposit --->"
      def _withdraw_member_account(self,name,id,amount):

            if self._list_of_members.has_key(id):
              self._list_of_members[id].withdraw_account(amount)
            else:
                print "No withdrwal >>> sys failure ??\n"

      def _show_member_account(self,name,id):
            if self._list_of_members.has_key(id):
               print "%s, %s, %d \n" % self._list_of_members[id].get_account()
            else:
                print "Unknown account \n"

      def _show_members_account(self):
            for item in self._list_of_members:
             print " %s, %s, %d \n" % self._list_of_members[item].get_account()
      def _member_account_exist(self, id):
            if (self._list_of_members.get(id, "none") !=  "none"):
               return True
            else:
               return False
      def show_member_ids(self):
          for i in self._list_of_members.keys():
              print "%s, \n" % i
      def show_members(self):
          for i in self._list_of_members.values():
              print "%s, %s, %d \n" % (i.get_account_name(),i.get_account_id(),i.get_account_balance())

k_list = members()

k_list._add_member('John','97',6000)
k_list._add_member('Kinuthia','72',8000)
k_list._add_member('Peter','46',16000)

k_list._deposit_member_account('John','97',1000)
k_list._withdraw_member_account('Kinuthia','72',2000)

k_list._add_member('David','100',10000)
k_list._show_member_account('John','97')
#print "=================================\n"
k_list._show_members_account()
k_list.show_member_ids()
k_list.show_members()
