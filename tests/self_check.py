import time
from yeelight_extras import Bulb, Group, flows, scenes

known_bulbs = [
    'gameroom-light-1',
    'gameroom-light-2',
    'gameroom-light-3',
    'gameroom-light-4'
]
group = []

print('TEST 1: Bulbs')
for b in known_bulbs:

    print(f'Checking {b} ...', end='\r')

    bulb = Bulb(b)
    try:
        bulb.turn_on()
        bulb.turn_off()
        time.sleep(1)
        bulb.turn_on()
        bulb.get_properties()
        print(f'Checking {bulb.address} ({bulb.ip})...ONLINE')
        group.append(bulb)
    except Exception as e:
        print(f'Checking {bulb.address} ({bulb.ip})...OFFLINE\n{e}')


print('TEST 2: Group')
g = Group(group)

print('Turn group ON.')
g.turn_on()
time.sleep(1)

print('Turn group OFF.')
g.turn_off()
time.sleep(1)

print('Turn group ON.')
g.turn_on()
time.sleep(1)

print('Turn group WHITE.')
g.set_color(255, 255, 255)
time.sleep(1)

print('Turn group RED.')
g.set_color(255, 0, 0)
time.sleep(1)

print('Turn group GREEN.')
g.set_color(0, 255, 0)
time.sleep(1)

print('Turn group BLUE.')
g.set_color(0, 0, 255)
time.sleep(1)

print('Set scene CAMPFIRE.')
g.set_scene('campfire')
time.sleep(5)

print('Set group DAYLIGHT.')
g.set_flow('daylight')
time.sleep(1)

print('Set scene NIGHT.')
g.set_scene('night')
time.sleep(1)

print('Set group DAYLIGHT.')
g.set_flow('daylight')
time.sleep(1)

print('Set group MOONLIT.')
g.set_scene('moonlit')
time.sleep(5)

print('Set group DAYLIGHT.')
g.set_flow('daylight')
time.sleep(1)

print('Set group GHOST_ENCOUNTER_FLOW.')
g.set_scene('ghost_encounter_1')
time.sleep(10)

print('Set group DAYLIGHT.')
g.set_flow('daylight')
time.sleep(1)

print('Self test complete.')
