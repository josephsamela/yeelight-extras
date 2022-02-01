from yeelight import discover_bulbs, flows, Bulb

bulb = Bulb(discover_bulbs()[0]['ip']) # Get the first bulb found. I only have one so this works.
bulb.set_brightness(100)

for flow in dir(flows):
    if '__' in flow:
        continue
    elif flow[0].isupper():
        continue
    else:
        try:
            eval('bulb.start_flow(flows.'+flow+'())')
            input('Displaying "'+flow+'" \t\t Press ENTER to continue...')
        except Exception as e:
            print(e)


