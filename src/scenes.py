import time

def night(bulbs, group):
    for b in bulbs:
        b.turn_off()
    return

def halloween_festival(bulbs, group):
    group.set_flow('streetlights')
    return

def moonlit(bulbs, group):

    moon = bulbs[3]

    for b in bulbs:
        b.turn_off()

    moon.set_color_temp(8000)
    moon.turn_on()
    moon.set_brightness(25)
    return

def ghost_encounter_1(bulbs, group):
    group.turn_on()
    group.set_color_temp(8000)
    speed = 0.2
    for b in bulbs:
        b.set_flow('ghost_encounter_flow', speed)
        time.sleep(speed)
    return

def ghost_encounter_2(bulbs, group):
    group.turn_on()
    group.set_color_temp(8000)
    speed = 1
    bulbs[0].set_flow('ghost_encounter_flow_2', speed)
    time.sleep(speed)
    bulbs[2].set_flow('ghost_encounter_flow_2', speed)
    time.sleep(speed)
    bulbs[1].set_flow('ghost_encounter_flow_2', speed)
    time.sleep(speed)
    bulbs[3].set_flow('ghost_encounter_flow_2', speed)
    return

def ghost_encounter_sw(bulbs, group):
    group.turn_on()
    group.set_color_temp(8000)
    speed = 0.25
    bl = 50
    bd = 0

    bulbs[0].set_brightness(bl)
    time.sleep(speed)
    bulbs[1].set_brightness(bd)
    time.sleep(speed)
    bulbs[2].set_brightness(bd)
    time.sleep(speed)
    bulbs[3].set_brightness(bd)       

def campfire(bulbs, group):
    group.turn_on()
    bulbs[0].set_flow('candle_flicker')
    bulbs[2].turn_off()
    bulbs[3].turn_off()
    bulbs[1].set_flow('candle_flicker')
