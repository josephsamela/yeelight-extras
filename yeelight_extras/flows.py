from yeelight.flow import Action, Flow, RGBTransition, TemperatureTransition
from yeelight.flows import *

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

def fireworks():
    '''
    Simulate beautiful firework bursts of color!

    :returns: An infinite Flow of bursting fireworks
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(0, 0, 0, brightness=1, duration=10),
        RGBTransition(0, 0, 0, brightness=1, duration=5000),
        RGBTransition(255, 0, 255, brightness=100, duration=1000),
        RGBTransition(0, 255, 255, brightness=100, duration=1000),
        RGBTransition(0, 0, 0, brightness=1, duration=1000),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def torch_flicker():
    """
    Simulate bright torch

    :returns: An infinite Flow consisting of 9 transitions.
    :rtype: Flow
    """
    transitions = [
        TemperatureTransition(degrees=2700, duration=800, brightness=80),
        TemperatureTransition(degrees=2000, duration=800, brightness=60),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2000, duration=800, brightness=90),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2000, duration=2400, brightness=80),
        TemperatureTransition(degrees=2700, duration=1200, brightness=100),
        TemperatureTransition(degrees=2000, duration=800, brightness=90),
        TemperatureTransition(degrees=2700, duration=400, brightness=100),
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)
