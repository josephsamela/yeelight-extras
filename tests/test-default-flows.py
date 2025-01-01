from yeelight_extras import Group, Bulb, flows

g1 = Bulb('gameroom1')
g2 = Bulb('gameroom2')
g3 = Bulb('gameroom3')
g4 = Bulb('gameroom4')
g = Group([g1, g2, g3, g4])

g.turn_on()
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
