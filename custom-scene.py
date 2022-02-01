import yeelight
import time

class Bulb(yeelight.Bulb):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.ip = self.discover_bulb_by_name(name)['ip']
        super().__init__(self.ip, *args, **kwargs)

    def discover_bulb_by_name(self, name):
        for bulb in yeelight.discover_bulbs():
            if bulb['capabilities']['name'] == name:
                return bulb

class Group:
    def __init__(self, bulbs):
        self.bulbs = bulbs

    # def __getattr__(self, method, *args, **kwargs):
    #     for bulb in self.bulbs:
    #         getattr(bulb, method)(*args, **kwargs)
    #     return self.result

    def __getattr__(self, method):
        print('hello')

    # def __getattribute__(self, method, *args, **kwargs):
    #     returns = []
    #     for bulb in object.__getattribute__(self, 'bulbs'):
    #         r = getattr(bulb, method)(*args, **kwargs)
    #         returns.append(r)
    #     return returns

if __name__ == '__main__':

    gameroom1 = Bulb('gameroom1')
    gameroom2 = Bulb('gameroom2')
    gameroom3 = Bulb('gameroom3')
    gameroom4 = Bulb('gameroom4')

    gameroom = Group([gameroom1, gameroom2, gameroom3, gameroom4])

    print(gameroom1.get_properties()['power'])
    print(gameroom2.get_properties()['power'])
    print(gameroom3.get_properties()['power'])
    print(gameroom4.get_properties()['power'])

    gameroom.toggle()

    print(gameroom1.get_properties()['power'])
    print(gameroom2.get_properties()['power'])
    print(gameroom3.get_properties()['power'])
    print(gameroom4.get_properties()['power'])

    print()

