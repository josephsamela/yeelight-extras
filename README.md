# yeelight-extras

I have a set of yeelight Smart LED light bulbs. Yeelight is a great brand because there's an [official Python Library from yeelight](https://yeelight.readthedocs.io/en/latest/) that allows you to control your bulbs and write custom flows in python! Unfortunately, it lacks basic features. For example:

* Creating and controlling a "Group" of bulbs.
* Connecting to bulbs by name instead of ip address.
* Setting colors using RGB *and* hexidecimal interchangably.
* Start flows by name (instead of passing flow object). 

I wrote this package `yeelight-extras` that extends the official library and adds in these extra features. Here's an example of how easy it is to control lights with my library.

```python
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
```

