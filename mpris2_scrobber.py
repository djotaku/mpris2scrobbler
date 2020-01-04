# using mpris2 from https://pypi.org/project/mpris2/

# configure mainloop (not required if you wont expect signals)
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

# you can use get_players_uri to get current running players uri
from mpris2 import get_players_uri
# next raise StopIteration if not found
uri = next(get_players_uri())

# create you player
from mpris2 import Player
player = Player(dbus_interface_info={'dbus_uri': uri})
 
print(uri)
print(player.Metadata) #current media data
print(player.Metadata.keys())
