from yeelight import flows

from yeelight_extras import Group, Bulb

g1 = Bulb('gameroom1')
g = Group([g1])

g.power_on()
g.set_brightness(100)

for flow in dir(flows):
    if '__' in flow:
        continue
    elif flow[0].isupper():
        continue
    else:
        try:
            eval('g.start_flow(flows.'+flow+'())')
            input('Displaying "'+flow+'" \t Press ENTER to continue...')
        except Exception as e:
            print(e)


