from helpers.switch import *
from ciscoconfparse import CiscoConfParse

network_switch = switch("sandbox-iosxr-1.cisco.com")
config = network_switch.info
print(type(config))

parse = CiscoConfParse(config, syntax='ios')

for intf_obj in parse.find_objects_w_child('^interface', '^\s+shutdown'):
    print("Shutdown: " + intf_obj.text)
