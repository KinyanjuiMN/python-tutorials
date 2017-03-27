import mammals
import birds
import sys
path = sys.path
print path[0]
print sys.argv[0]

m = mammals.mammals()
b = birds.birds()

m._init_("Hyna \n")
b._init_()

m._show_mammal()
b._show_bird()
mo = sys.modules
for item in mo:
   print item + "\n"

print sys.prefix + "\n"
print sys.version + "\n"
