import time

def ghost_encounter_1(bulbs, group, complete):
    group.turn_on()
    group.set_color_temp(8000)
    speed = 0.2
    for b in bulbs:
        b.set_flow('ghost_encounter_flow', speed)
        time.sleep(speed)
    return

def ghost_encounter_2(bulbs, group, complete):
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

def ghost_encounter_sw(bulbs, group, complete):
    group.turn_on()
    group.set_color_temp(8000)
    # group.stop_music()
    # group.start_music()
    speed = 0.25
    bl = 50
    bd = 0
    while not complete.is_set():
        bulbs[0].set_brightness(bl)
        bulbs[1].set_brightness(bd)
        bulbs[2].set_brightness(bd)
        bulbs[3].set_brightness(bd)       
        time.sleep(speed)
        bulbs[0].set_brightness(bd)
        bulbs[1].set_brightness(bl)
        bulbs[2].set_brightness(bd)
        bulbs[3].set_brightness(bd)
        time.sleep(speed)
        bulbs[0].set_brightness(bd)
        bulbs[1].set_brightness(bd)
        bulbs[2].set_brightness(bl)
        bulbs[3].set_brightness(bd)
        time.sleep(speed)
        bulbs[0].set_brightness(bd)
        bulbs[1].set_brightness(bd)
        bulbs[2].set_brightness(bd)
        bulbs[3].set_brightness(bl)
        time.sleep(speed)
