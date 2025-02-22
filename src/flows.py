from yeelight.flow import Action, Flow, RGBTransition, TemperatureTransition, SleepTransition, HSVTransition
from yeelight.flows import *

import random

def forest_canopy():
    '''
    Simulate dappeling sunlight through forest canopy.

    :returns: An infinite Flow consisting of white, green and yello
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(174, 255, 174, duration=5000, brightness=100), # Green
        RGBTransition(251, 255, 222, duration=5000, brightness=100), # Sunlight yellow
        RGBTransition(149, 208, 155, duration=5000, brightness=100)  # Dark green
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def candy_cane_forest():
    '''
    Simulate dappeling sunlight through forest canopy.

    :returns: An infinite Flow consisting of white, green and yello
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(237, 100, 136, duration=5000, brightness=100),
        RGBTransition(251, 255, 222, duration=5000, brightness=100), # Sunlight yellow
        RGBTransition(201, 50, 53, duration=5000, brightness=100) 
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)


def fireworks():
    '''
    Simulate beautiful firework bursts of color!

    :returns: An infinite Flow of bursting fireworks
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(255, 0, 0, brightness=1, duration=5000),
        RGBTransition(0, 0, 0, brightness=1, duration=1),
        RGBTransition(0, 0, 0, brightness=1, duration=5000),

        RGBTransition(0, 255, 0, brightness=1, duration=5000),
        RGBTransition(0, 0, 0, brightness=1, duration=1),
        RGBTransition(0, 0, 0, brightness=1, duration=5000),

        RGBTransition(0, 0, 255, brightness=1, duration=5000),
        RGBTransition(0, 0, 0, brightness=1, duration=1),
        RGBTransition(0, 0, 0, brightness=1, duration=5000),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def torch_flicker():
    '''
    Simulate bright torch

    :returns: An infinite Flow consisting of 9 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=2700, duration=800, brightness=80),
        TemperatureTransition(degrees=2700, duration=800, brightness=70),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2700, duration=800, brightness=90),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2700, duration=2400, brightness=80),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2700, duration=800, brightness=90),
        TemperatureTransition(degrees=2700, duration=400, brightness=100),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def lightning_storm():
    '''
    Simulate crackling lightning storm

    :returns: An infinite Flow of crackling lightning.
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(12, 13, 29, brightness=100, duration=1000),
        RGBTransition(121, 164, 255, brightness=100, duration=250),
        RGBTransition(87, 100, 177, brightness=100, duration=100),
        RGBTransition(255, 255, 255, brightness=1, duration=1),
        RGBTransition(12, 13, 29, brightness=100, duration=250),
        RGBTransition(151, 253, 255, brightness=100, duration=50),
        RGBTransition(100, 127, 218, brightness=10, duration=1000),
        RGBTransition(255, 255, 255, brightness=1, duration=5000)
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def sparkler():
    '''
    Simulate white & gold sparkler

    :returns: An infinite Flow of sparkler
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(239, 219, 157, brightness=100, duration=75),
        RGBTransition(239, 219, 157, brightness=80, duration=75),
        RGBTransition(241, 237, 180, brightness=100, duration=75),
        RGBTransition(241, 237, 180, brightness=80, duration=75),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def color_burst():
    '''
    Burst of random color

    :returns: A single Flow that bursts random color
    :rtype: Flow
    '''
    duration = 2500
    color = random.choice([
        (255, 0, 0),   # red
        (0, 255, 0),   # green
        (0, 0, 255),   # blue
        (255, 0, 255), # purple
    ])
    r = color[0]
    g = color[1]
    b = color[2]

    transitions = [
        RGBTransition(0, 0, 0, brightness=1, duration=duration),
        RGBTransition(r, g, b, brightness=100, duration=duration),
        RGBTransition(0, 0, 0, brightness=1, duration=duration),
    ]
    return Flow(count=0, action=Action.stay, transitions=transitions)

def daylight():
    '''
    Show regular daylight

    :returns: An infinite Flow consisting of 1 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=4500, duration=1000, brightness=100),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def overcast():
    '''
    Overcast daytime

    :returns: An infinite Flow consisting of 1 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=6500, duration=1000, brightness=80),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def cozyroom():
    '''
    Light in color of a cozy room

    :returns: An infinite Flow consisting of 1 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=4000, duration=1000, brightness=75),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def streetlights():
    '''
    Dim warm lights like streetlights at dusk

    :returns: An infinite Flow consisting of 1 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=4000, duration=1000, brightness=10),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def swealtering_daylight():
    '''
    Simulate a bright swealtering sun

    :returns: An infinite Flow consisting of 9 transitions.
    :rtype: Flow
    '''
    transitions = [
        TemperatureTransition(degrees=5000, duration=5000, brightness=70),
        TemperatureTransition(degrees=4500, duration=5000, brightness=50),
        TemperatureTransition(degrees=5000, duration=5000, brightness=75),
        TemperatureTransition(degrees=5200, duration=5000, brightness=60),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def infernal():
    '''
    As you enter the mouth of hell the red sky churns above you.

    :returns: An infinite Flow consisting of 3 transitions.
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(255, 0, 0, brightness=100, duration=1000),
        RGBTransition(223, 49, 2, brightness=90, duration=1000),
        RGBTransition(255, 0, 0, brightness=80, duration=1000),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def crevasse():
    '''
    Trapped beneath the ice weak sunlight illuminates your path.

    :returns: An infinite Flow consisting of 3 transitions.
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(14, 179, 230, brightness=100, duration=1000),
        RGBTransition(0, 238, 255, brightness=90, duration=1000),
        RGBTransition(0, 164, 176, brightness=80, duration=1000),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def tundra():
    '''
    Hiking across the endless expanse of the icy tundra.

    :returns: An infinite Flow consisting of 3 transitions.
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(176, 210, 255, brightness=80, duration=1000),
        RGBTransition(255, 255, 255, brightness=100, duration=2500),
        RGBTransition(105, 170, 255, brightness=100, duration=3000),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def ghost_encounter_flow(speed):
    '''
    Luminescent ethereal energy spins around you.

    :returns: An infinite Flow consisting of 9 transitions.
    :rtype: Flow
    '''
    
    duration_light = speed*1000
    duration_dark = duration_light*4

    transitions = [
        TemperatureTransition(degrees=8000, duration=duration_dark, brightness=0),
        TemperatureTransition(degrees=8000, duration=duration_light, brightness=50),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def ghost_encounter_flow_2(speed):
    '''
    Luminescent ethereal energy spins around you.

    :returns: An infinite Flow consisting of 9 transitions.
    :rtype: Flow
    '''
    
    duration_light = speed*1000
    duration_dark = duration_light/2

    transitions = [
        TemperatureTransition(degrees=8000, duration=duration_dark, brightness=0),
        TemperatureTransition(degrees=8000, duration=duration_light, brightness=50),
        TemperatureTransition(degrees=8000, duration=duration_dark, brightness=0),
        TemperatureTransition(degrees=8000, duration=duration_dark*4, brightness=0),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)
