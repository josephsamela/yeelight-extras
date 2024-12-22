from .yeelight_extras import Bulb, Group
import time

t0 = time.time()

g1 = Bulb('gameroom1')
g2 = Bulb('gameroom2')
g3 = Bulb('gameroom3')
g4 = Bulb('gameroom4')

g = Group([g1, g2, g3, g4])

print(g.get_property('power'))
g.toggle()
print(g.get_property('current_brightness'))
g.set_brightness(50)
print(g.get_property('current_brightness'))
g.set_brightness(100)
print(g.get_property('current_brightness'))
g.toggle()
print(g.get_property('power'))

print(f'Completed in {time.time() - t0} seconds')
