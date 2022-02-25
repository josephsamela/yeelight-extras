import yeelight
import socket
from . import flows

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
            'gameroom1': '192.168.1.40',
            'gameroom2': '192.168.1.41',
            'gameroom3': '192.168.1.42',
            'gameroom4': '192.168.1.43'
        }
        if self._valid_ip(address):
            self.ip = address
        else:
            if address in self.known_bulbs:
                self.ip = self.known_bulbs[address]
            else:
                self.ip = self._discover_bulb_by_name(address)['ip']
        super().__init__(self.ip, *args, **kwargs)

    def power_on(self):
        return self._setState('on')

    def power_off(self):
        return self._setState('off')

    def get_power(self):
        return self.get_properties()['power']

    def set_flow(self, flow_name):
        return self.start_flow(flow=getattr(flows, flow_name)())

    def set_color(self, r, g=0, b=0):
        '''
        Set bulb color with rgb or hexidecimal color code.
        '''
        if isinstance(r, str) and r[0] == '#':
            r,g,b = tuple(int(r[1:][i:i+2], 16) for i in (0, 2, 4))
        return self.set_rgb(r,g,b)

    def _setState(self, requested_state):
        current_state = self.get_properties()['power']
        if current_state  == requested_state:
            return 'ok'
        elif current_state != requested_state:
            return self.toggle()
        else:
            raise Exception('Could not communicate with light')

    def _discover_bulb_by_name(self, name):
        for bulb in yeelight.discover_bulbs():
            if bulb['capabilities']['name'] == name:
                return bulb

    def _valid_ip(self, address):
        try: 
            socket.inet_aton(address)
            return True
        except:
            return False

class Group:
    '''
    This class allows you to control groups of bulbs. Whatever command
    you envoke for the groups applies to all bulbs in the group. For
    example, `group.toggle()` will toggle all bulbs in the group.

    Example Usage:
        kitchen = Group([bulb1, bulb2, bulb3])
        kitchen.toggle()
        kitvhen.set_brightness(50)

    Parameters:
        bulbs (list): A list of Bulb() objects. ie. [b1, b2, b3]
    '''
    def __init__(self, bulbs):
        self.bulbs = bulbs
    def __getattr__(self, method):
        def impl(*args, **kwargs):
            responses = []
            for bulb in self.bulbs:
                rsp = getattr(bulb, method)(*args, **kwargs)
                responses.append(rsp)
            return responses
        return impl
