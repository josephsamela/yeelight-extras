from yeelight.flow import Action
from yeelight.flow import Flow
from yeelight.flow import RGBTransition

def forestCanopy():
    '''
    Simulate dappeling sunlight through forest canopy.

    :returns: An infinite Flow consisting of white, green and yello
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(229, 255, 204, duration=300, brightness=100),
        RGBTransition(255, 255, 204, duration=300, brightness=100),
        RGBTransition(255, 255, 255, duration=300, brightness=100)
    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

def fireworks():
    '''
    Simulate beautiful firework bursts of color!

    :returns: An infinite Flow of bursting fireworks
    :rtype: Flow
    '''
    transitions = [
        RGBTransition(255, 0, 0, brightness=100, duration=1000), # Red
        RGBTransition(0, 0, 0, brightness=0, duration=1000),
        RGBTransition(0, 255, 0, brightness=100, duration=1000), # Green
        RGBTransition(0, 0, 0, brightness=0, duration=1000),
        RGBTransition(0, 0, 255, brightness=100, duration=1000), # Blue
        RGBTransition(0, 0, 0, brightness=0, duration=1000),

    ]
    return Flow(count=0, action=Action.recover, transitions=transitions)

