from yeelight_extras import Bulb, Group

b1 = Bulb('bulb1')              # Connect to bulb by name
b2 = Bulb('192.168.1.54')       # Connect to bulb by ip address

g = Group([b1,b2])              # Create a group

g.turn_on()                     # Turn ON all bulbs in group

print(g.get_property('power'))  # Get bulb property by name 
                                # Groups with multiple bulbs will return list (ie. ['on', 'on'])

g.set_color('#88a7ff')          # Set group to hex color
g.set_color(255, 0, 0)          # Set group to RGB color
g.set_flow('candle_flicker')    # Set group to display flow by name

g.turn_off()                    # Turn OFF all bulbs in group
