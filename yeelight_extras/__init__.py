import yeelight
import socket
import time
import threading
import requests
from . import flows, scenes

class Bulb(yeelight.Bulb):
    '''
    This class extends `yeelight.Bulb` to add auto-connection features! 
    When creating an object of this class, pass an "address" (name or ip-address) 
    and it will auto-connect to the correct bulb.

    Example usage:
        b1 = Bulb('basement1')
        b2 = Bulb('kitchen-overhead')
        b3 = Bulb('192.168.1.54)

    Parameters:
        address (str): Pass an "address" which can be either the bulb ip
            address (ie. 192.168.1.50) or name (ie. gameroom1).
    '''
    def __init__(self, address, *args, **kwargs):
        self.known_bulbs = {
            'gameroom-light-1': '192.168.1.21',
            'gameroom-light-2': '192.168.1.22',
            'gameroom-light-3': '192.168.1.23',
            'gameroom-light-4': '192.168.1.24'
        }
        self.address = address
        if self._valid_ip(address):
            self.ip = address
        else:
            if address in self.known_bulbs:
                self.ip = self.known_bulbs[address]
            else:
                self.ip = self._discover_bulb_by_name(address)['ip']
        super().__init__(self.ip, *args, **kwargs)
        self._self_check()

    def get_property(self, property_name):
        properties = self.get_properties()
        if property_name in properties:
            return properties[property_name]
        else:
            raise Exception(f'This bulb has no property called "{property_name}"')

    def set_flow(self, flow_name, *args, **kwargs):
        '''
        Set bulb to run flow.
        '''
        self.turn_on()
        return self.start_flow(flow=getattr(flows, flow_name)(*args, **kwargs))

    def set_color(self, r, g=0, b=0):
        '''
        Set bulb color with rgb or hexidecimal color code.
        '''
        if isinstance(r, str) and r[0] == '#':
            r,g,b = tuple(int(r[1:][i:i+2], 16) for i in (0, 2, 4))
        return self.set_rgb(r,g,b)

    def send_command(self, method, params=None, retries=10):
        attempt = 0
        while attempt < retries:
            try:
                time.sleep(attempt/4)
                attempt+=1
                return super().send_command(method, params)
            except Exception as e:
                print(f'Attempt {attempt}/{retries} failed: {e}')

    def _discover_bulb_by_name(self, name):
        for bulb in yeelight.discover_bulbs():
            if bulb['capabilities']['name'] == name:
                return bulb

    def _self_check(self):
        try:
            self.get_properties()
        except Exception as e:
            raise ConnectionError(f'Device {self.address} ({self.ip}) is offline. {e}')

    def _valid_ip(self, address):
        try: 
            socket.inet_aton(address)
            return True
        except:
            return False

class Group:
    '''
    This class allows you to control groups of bulbs. Whatever method
    you envoke of the group applies to all bulbs in the group. For
    example, `group.turn_on()` will turn on all bulbs in the group.

    Example Usage:
        kitchen = Group([bulb1, bulb2, bulb3])
        kitchen.turn_on()
        kitchen.set_brightness(50)
        kitchen.turn_off()

    Parameters:
        bulbs (list): A list of Bulb() objects. ie. [b1, b2, b3]
    '''
    def __init__(self, bulbs):
        self.bulbs = bulbs
        self.active_scene = None
    def __getattr__(self, method):
        def impl(*args, **kwargs):
            responses = []
            for bulb in self.bulbs:
                rsp = getattr(bulb, method)(*args, **kwargs)
                responses.append(rsp)
            return responses
        return impl

    def set_scene(self, scene_name):
        if self.active_scene:
            self.stop_scene()
        self.active_scene = scene_name
        getattr(scenes, scene_name)(self.bulbs, self)

    def stop_scene(self):
        self.active_scene = None
        self.turn_on()
