import time

def ghost_encounter(bulbs, group, complete):
    group.turn_on()
    group.set_color_temp(8000)
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
