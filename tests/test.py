from yeelight_extras import Bulb, Group
import time

t0 = time.time()

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

print(gameroom1.get_properties()['current_brightness'])
print(gameroom2.get_properties()['current_brightness'])
print(gameroom3.get_properties()['current_brightness'])
print(gameroom4.get_properties()['current_brightness'])

gameroom.set_brightness(50)

print(gameroom1.get_properties()['current_brightness'])
print(gameroom2.get_properties()['current_brightness'])
print(gameroom3.get_properties()['current_brightness'])
print(gameroom4.get_properties()['current_brightness'])

gameroom.set_brightness(100)

print(gameroom1.get_properties()['current_brightness'])
print(gameroom2.get_properties()['current_brightness'])
print(gameroom3.get_properties()['current_brightness'])
print(gameroom4.get_properties()['current_brightness'])

gameroom.toggle()

print(gameroom1.get_properties()['power'])
print(gameroom2.get_properties()['power'])
print(gameroom3.get_properties()['power'])
print(gameroom4.get_properties()['power'])

print(f'Completed in {time.time() - t0} seconds')
