# from . import Cperson

from People.Cperson import person
# from Accounts.Account import account
# Account class has issues with import


per = person()

per._init_("Kinuthia","203030")

per._show_person()
