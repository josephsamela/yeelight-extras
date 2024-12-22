import time
import requests

from .flows import streetlights

def night(bulbs, group, complete):
    for b in bulbs:
        b.turn_off()
    response = requests.request('get', 'http://192.168.1.35/cm?cmnd=Power%20OFF')
    return

def halloween_festival(bulbs, group, complete):
    group.set_flow('streetlights')
    response = requests.request('get', 'http://192.168.1.35/cm?cmnd=Power%20ON')
    return

def moonlit(bulbs, group, complete):

    moon = bulbs[3]

    for b in bulbs:
        b.turn_off()

    moon.set_color_temp(8000)
    moon.turn_on()
    moon.set_brightness(25)
    return

def ghost_encounter_1(bulbs, group, complete):
    group.turn_on()
    group.set_color_temp(8000)
    speed = 0.2
    for b in bulbs:
        b.set_flow('ghost_encounter_flow', speed)
        time.sleep(speed)
    return

def ghost_encounter_2(bulbs, group, complete):
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

def campfire(bulbs, group, complete):
    group.turn_on()
    bulbs[0].set_flow('candle_flicker')
    bulbs[2].turn_off()
    bulbs[3].turn_off()
    bulbs[1].set_flow('candle_flicker')
    return
